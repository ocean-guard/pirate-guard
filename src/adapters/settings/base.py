from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from pydantic_settings import BaseSettings, SettingsConfigDict


class OceanGuardExchange(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class OceanGuardSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
