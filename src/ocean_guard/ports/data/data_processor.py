from abc import ABC, abstractmethod


class Processor(ABC):
    @abstractmethod
    async def listen(self):
        pass
