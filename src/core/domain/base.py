from dataclasses import dataclass
from typing import Annotated, NewType, TypeVar

from annotated_types import Ge

from ocean_guard.core.domain.time import DateTime

# Basic type for IDs
ID = NewType("ID", Annotated[int, Ge(0)])

# Default ID for entities that don't have one
UNDEFINED_ID = ID(0)


@dataclass(eq=True, frozen=True)
class Value:
    pass


@dataclass(eq=True, frozen=True)
class Entity(Value):
    id: ID
    created_at: DateTime


DomainType = TypeVar("DomainType", bound=Value | Entity)
ValueType = TypeVar("ValueType", bound=Value)
EntityType = TypeVar("EntityType", bound=Entity)
