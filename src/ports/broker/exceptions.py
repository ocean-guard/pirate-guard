from typing import Any

from ocean_guard.core.domain.exception import OceanGuardException
from ocean_guard.core.domain.values.localized_str import LStr


class ProducerException(OceanGuardException):
    def __init__(self, invalid_message: Any):
        self.invalid_value = invalid_message

        super().__init__(
            cause=LStr(
                en_UK=f"Error while producing: {self.invalid_value}`",
            )
        )


class ConsumerException(OceanGuardException):
    def __init__(self, invalid_message: Any):
        self.invalid_value = invalid_message

        super().__init__(
            cause=LStr(
                en_UK=f"Error while consuming: {self.invalid_value}`",
            )
        )
