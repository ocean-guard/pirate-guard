from typing import Any, override

from ocean_guard.core.domain.values.message import Message
from ocean_guard.ports.broker.producer import Producer
from ocean_guard.ports.data.data_retriever import Retriever


class ShipRetriever(Retriever):
    def __init__(self, source: Any, producer: Producer):
        self.__source = source
        self.__producer = producer

    @override
    async def retrieve(self):
        data = self.__load_data_from_source()
        for response in data:
            msg = Message(key=response["ship_name"], value=response["flag"])
            self.__producer.produce(msg)

    def __load_data_from_source(self):
        pass
