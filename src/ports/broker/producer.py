from abc import ABC, abstractmethod

from ocean_guard.core.domain.values.message import Message


class Producer(ABC):
    @abstractmethod
    def produce(self, message: Message):
        pass
