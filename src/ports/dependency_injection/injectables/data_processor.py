from dataclasses import dataclass

from ocean_guard.ports.data.data_processor import Processor
from ocean_guard.ports.dependency_injection.injectable import Injectable


@dataclass(eq=True, frozen=True)
class DataProcessor(Injectable):
    processor: Processor
