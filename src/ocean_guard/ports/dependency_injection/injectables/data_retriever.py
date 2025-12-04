from dataclasses import dataclass

from ocean_guard.ports.data.data_retriever import Retriever
from ocean_guard.ports.dependency_injection.injectable import Injectable


@dataclass(eq=True, frozen=True)
class DataRetriever(Injectable):
    retriever: Retriever
