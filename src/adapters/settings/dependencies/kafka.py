from pydantic_settings import SettingsConfigDict

from ocean_guard.adapters.settings.base import OceanGuardSettings


class KafkaProducerSettings(OceanGuardSettings):
    model_config = SettingsConfigDict(env_prefix="KAFKA_PRODUCER_")

    topic: str
    bootstrap_servers: str
    acks: str

    @property
    def config(self) -> dict:
        return {
            "bootstrap.servers": self.bootstrap_servers,
            "acks": self.acks,
        }


class KafkaConsumerSettings(OceanGuardSettings):
    model_config = SettingsConfigDict(env_prefix="KAFKA_CONSUMER_")

    topic: str
    bootstrap_servers: str
    group_id: str
    auto_offset_reset: str

    @property
    def config(self) -> dict:
        return {
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": self.group_id,
            "auto.offset.reset": self.auto_offset_reset,
        }
