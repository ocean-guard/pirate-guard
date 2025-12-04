from abc import ABC, abstractmethod
from io import BytesIO
from pathlib import Path


class Storage(ABC):
    @abstractmethod
    def save_bytes_object(self, filename: Path, data: BytesIO, length: int) -> None:
        pass

    @abstractmethod
    def load_bytes_object(self, filename: Path) -> bytes:
        pass

    @abstractmethod
    def list_objects(self) -> list[Path]:
        pass

    @abstractmethod
    def add_tag(self, object_name: Path, tag_key: str, tag_value: str):
        pass

    @abstractmethod
    def get_tag(self, object_name: Path):
        pass
