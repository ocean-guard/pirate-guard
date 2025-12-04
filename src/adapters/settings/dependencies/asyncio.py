from pydantic_settings import SettingsConfigDict

from ocean_guard.adapters.settings.base import OceanGuardSettings


class AsyncIOSettings(OceanGuardSettings):
    model_config = SettingsConfigDict(env_prefix="ASYNCIO_")

    chunk_size: int
