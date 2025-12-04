from pydantic import AnyUrl
from pydantic_settings import SettingsConfigDict

from ocean_guard.adapters.settings.base import OceanGuardSettings


class MinIOSettings(OceanGuardSettings):
    model_config = SettingsConfigDict(env_prefix="MINIO_")

    server_address: AnyUrl

    root_user: str
    root_password: str

    secure: bool

    bucket_name: str
