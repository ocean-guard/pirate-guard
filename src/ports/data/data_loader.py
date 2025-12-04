from abc import ABC, abstractmethod


class DataLoader(ABC):
    @abstractmethod
    async def load(self):
        pass
