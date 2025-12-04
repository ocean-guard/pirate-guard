from dataclasses import dataclass

from ocean_guard.ports.broker.producer import Producer
from ocean_guard.ports.dependency_injection.injectable import Injectable


@dataclass(eq=True, frozen=True)
class BrokerProducer(Injectable):
    producer: Producer
