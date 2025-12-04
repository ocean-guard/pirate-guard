from typing import override

from ocean_guard.adapters.broker.asyncio.asyncio_broker import AsyncIOBroker
from ocean_guard.core.domain.values.message import Message
from ocean_guard.ports.broker.consumer import Consumer


class AsyncIOConsumer(Consumer):
    def __init__(self, broker: AsyncIOBroker):
        self.__broker = broker

    @override
    async def consume(self) -> Message:
        await self.__broker
        message = self.__broker.publish_one()
        return message

    @override
    async def consume_batch(self) -> list[Message]:
        await self.__broker
        chunk = self.__broker.publish_many()
        return chunk
