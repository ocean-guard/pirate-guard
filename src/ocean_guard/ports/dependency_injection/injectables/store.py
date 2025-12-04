from dataclasses import dataclass

from ocean_guard.ports.dependency_injection.injectable import Injectable
from ocean_guard.ports.storage.storage import Storage


@dataclass(eq=True, frozen=True)
class Store(Injectable):
    storage: Storage
