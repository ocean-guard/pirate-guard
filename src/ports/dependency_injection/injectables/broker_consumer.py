from dataclasses import dataclass

from ocean_guard.ports.broker.consumer import Consumer
from ocean_guard.ports.dependency_injection.injectable import Injectable


@dataclass(eq=True, frozen=True)
class BrokerConsumer(Injectable):
    consumer: Consumer
