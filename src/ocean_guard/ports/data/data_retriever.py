from abc import abstractmethod, ABC


class Retriever(ABC):
    @abstractmethod
    async def retrieve(self):
        pass
