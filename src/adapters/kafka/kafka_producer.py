from typing import Any, override

import confluent_kafka

from ocean_guard.adapters.broker.kafka.kafka_serialization import (
    KafkaMessage,
    KafkaSerializer,
    KafkaStringSerializer,
)
from ocean_guard.adapters.settings.dependencies.kafka import KafkaProducerSettings
from ocean_guard.core.domain.values.message import Message
from ocean_guard.ports.broker.exceptions import ProducerException
from ocean_guard.ports.broker.producer import Producer


class KafkaProducerException(ProducerException):
    def __init__(self, message: KafkaMessage, topic: str):
        super().__init__(invalid_message=f"{topic}: {message.error()}")


class KafkaProducer(Producer):
    def __init__(self, settings: KafkaProducerSettings, serializer: KafkaSerializer):
        self.__topic = settings.topic

        self.__key_serializer = KafkaStringSerializer()
        self.__value_serializer = serializer
        self.__producer = confluent_kafka.Producer(settings.config)

    def __del__(self):
        # It is necessary to call flush() before termination.
        # The conditional ensures it runs only if the kafka producer is correctly initialized.
        # See: https://github.com/confluentinc/confluent-kafka-python/issues/16
        if self.__producer:
            self.__producer.flush()

    @override
    def produce(self, message: Message):
        serialized_key = self.__serialize_key(message.key)
        serialized_value = self.__serialize_value(message.value)
        timestamp = round(message.emitted_at.to_timestamp())

        self.__producer.produce(topic=self.__topic, key=serialized_key, value=serialized_value, timestamp=timestamp)

        # It is necessary to call poll() after a produce() call.
        # See: https://github.com/confluentinc/confluent-kafka-python/issues/16
        self.__producer.poll()

    def __serialize_key(self, key: str):
        return self.__key_serializer(key)

    def __serialize_value(self, value: Any):
        return self.__value_serializer(value)
