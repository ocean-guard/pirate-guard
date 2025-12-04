from typing import cast, override

import confluent_kafka

from ocean_guard.adapters.broker.kafka.kafka_serialization import (
    KafkaDeserializer,
    KafkaMessage,
    KafkaStringDeserializer,
)
from ocean_guard.adapters.settings.dependencies.kafka import KafkaConsumerSettings
from ocean_guard.core.domain.time import DateTime
from ocean_guard.core.domain.values.message import Message
from ocean_guard.ports.broker.consumer import Consumer
from ocean_guard.ports.broker.exceptions import ConsumerException


class KafkaConsumerException(ConsumerException):
    def __init__(self, message: KafkaMessage, topic: str):
        super().__init__(invalid_message=f"{topic}: {message.error()}")


class KafkaConsumer(Consumer):
    def __init__(self, settings: KafkaConsumerSettings, deserializer: KafkaDeserializer, batch_size: int = 100):
        self.__topic = settings.topic
        self.__value_deserializer = deserializer
        self.__key_deserializer = KafkaStringDeserializer()

        self.__batch_size = batch_size

        self.__consumer = confluent_kafka.Consumer(settings.config)
        self.__consumer.subscribe([self.__topic])

    @override
    async def consume(self) -> Message:
        msg = cast(KafkaMessage, self.__consumer.poll())

        if msg.error():
            raise KafkaConsumerException(message=msg, topic=self.__topic)

        return self.__deserialize_message(msg)

    @override
    async def consume_batch(self) -> list[Message]:
        return [await self.consume() for _ in range(self.__batch_size)]

    def __deserialize_message(self, message: KafkaMessage) -> Message:
        deserialized_key = self.__deserialize_key(message.key())
        deserialized_value = self.__deserialize_value(message.value())
        emitted_at = self.__recover_message_creation(message)
        return Message(key=deserialized_key, value=deserialized_value, emitted_at=emitted_at)

    @staticmethod
    def __recover_message_creation(message: KafkaMessage) -> DateTime:
        timestamp_type, timestamp = message.timestamp()
        return DateTime.from_raw_timestamp(timestamp)

    def __deserialize_key(self, key):
        return self.__key_deserializer(key)

    def __deserialize_value(self, value):
        return self.__value_deserializer(value)
