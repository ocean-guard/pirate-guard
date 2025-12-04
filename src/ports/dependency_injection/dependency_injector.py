from abc import ABC, abstractmethod
from typing import Generic

from ocean_guard.ports.dependency_injection.injectable import InjectableType


class DependencyInjector(ABC, Generic[InjectableType]):
    @abstractmethod
    def build(self) -> InjectableType:
        pass
