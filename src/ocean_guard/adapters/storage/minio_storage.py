import logging
from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import override

from minio import Minio
from minio.commonconfig import Tags

from ocean_guard.adapters.settings.dependencies.minio import MinIOSettings
from ocean_guard.core.domain.exception import OceanGuardException
from ocean_guard.core.domain.values.localized_str import LStr
from ocean_guard.ports.storage.storage import Storage


class InvalidMinioBucketException(OceanGuardException):
    def __init__(self, bucket_name: str):
        super().__init__(LStr(f"Invalid minio bucket {bucket_name}"))


class MinioStorageAdapter(Storage):
    def __init__(self, settings: MinIOSettings):
        self.__bucket_name = settings.bucket_name

        self.__client = Minio(
            str(settings.server_address),
            access_key=settings.root_user,
            secret_key=settings.root_password,
            secure=settings.secure,
        )

        self.__create_bucket_if_doesnt_exist()

    @override
    def save_bytes_object(self, filename: Path, data: BytesIO, length: int) -> None:
        prefix = Path(datetime.now().strftime("%Y-%m-%d"))

        tags = Tags.new_object_tags()
        tags["processed"] = "unprocessed"

        self.__client.put_object(
            bucket_name=self.__bucket_name,
            object_name=str(prefix.joinpath(filename)),
            data=data,
            length=length,
            content_type="application/json",
            tags=tags,
        )

        logging.warning("Saved bytes object to minio")

    @override
    def load_bytes_object(self, filename: Path) -> bytes:
        response = self.__client.get_object(
            bucket_name=self.__bucket_name,
            object_name=str(filename),
        )
        content = response.read()

        response.close()
        response.release_conn()

        return content

    @override
    def list_objects(self) -> list[Path]:
        return [Path(i.object_name) for i in self.__client.list_objects(bucket_name=self.__bucket_name, recursive=True)]

    @override
    def add_tag(self, object_name: Path, tag_key: str, tag_value: str):
        tag = Tags.new_object_tags()
        tag[tag_key] = tag_value

        self.__client.set_object_tags(bucket_name=self.__bucket_name, object_name=str(object_name), tags=tag)

    @override
    def get_tag(self, object_name: Path):
        return self.__client.get_object_tags(bucket_name=self.__bucket_name, object_name=str(object_name))

    def __get_bucket_names(self) -> list[str]:
        return [bucket.name for bucket in self.__client.list_buckets()]

    def __create_bucket_if_doesnt_exist(self):
        if self.__bucket_name not in self.__get_bucket_names():
            self.__create_bucket(self.__bucket_name)

    def __create_bucket(self, bucket_name: str):
        self.__client.make_bucket(bucket_name)
