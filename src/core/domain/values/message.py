from dataclasses import dataclass
from typing import Any

from ocean_guard.core.domain.time import DateTime


@dataclass(frozen=True)
class Message:
    key: str
    value: Any
    emitted_at: DateTime
