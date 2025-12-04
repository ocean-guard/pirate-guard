from abc import ABC, abstractmethod

from ocean_guard.core.domain.values.message import Message


class Consumer(ABC):
    @abstractmethod
    async def consume(self) -> Message:
        pass

    @abstractmethod
    async def consume_batch(self) -> list[Message]:
        pass
