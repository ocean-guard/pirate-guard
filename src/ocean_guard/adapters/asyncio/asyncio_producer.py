from typing import override

from ocean_guard.adapters.broker.asyncio.asyncio_broker import AsyncIOBroker
from ocean_guard.core.domain.values.message import Message
from ocean_guard.ports.broker.producer import Producer


class AsyncIOProducer(Producer):
    def __init__(self, broker: AsyncIOBroker):
        self.__broker = broker

    @override
    def produce(self, message: Message):
        self.__broker.send(message)
