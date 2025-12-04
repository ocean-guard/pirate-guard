import asyncio

from ocean_guard.adapters.settings.dependencies.asyncio import AsyncIOSettings
from ocean_guard.core.domain.values.message import Message


class AsyncIOBroker:
    def __init__(self, event, buffer_limit: int):
        self.__event = event

        self.__buffer_limit = buffer_limit
        self.__buffer: list = []

    def __await__(self):
        yield from self.__event.wait().__await__()

    @staticmethod
    async def __create_event() -> asyncio.Event:
        event = asyncio.Event()
        return event

    @classmethod
    async def init(cls, settings: AsyncIOSettings) -> "AsyncIOBroker":
        event = await AsyncIOBroker.__create_event()
        return AsyncIOBroker(event, settings.chunk_size)

    def send(self, item):
        self.__buffer.append(item)

        if self.__can_publish():
            self.__event.set()

    def publish_many(self) -> list[Message]:
        chunk = self.__buffer[: self.__buffer_limit].copy()
        del self.__buffer[: self.__buffer_limit]

        if self.__can_clear():
            self.__event.clear()

        return chunk

    def publish_one(self) -> Message:
        message = self.__buffer[0]
        del self.__buffer[0]

        if self.__can_clear():
            self.__event.clear()

        return message

    def __can_publish(self) -> bool:
        return len(self.__buffer) > self.__buffer_limit

    def __can_clear(self) -> bool:
        return len(self.__buffer) < self.__buffer_limit
