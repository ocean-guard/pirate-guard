from datetime import datetime, timedelta, timezone, tzinfo
from typing import Annotated, NewType, cast

from annotated_types import Ge, Timezone
from dateutil import parser

DEFAULT_TIMEZONE: tzinfo = timezone.utc


OGDateTime = NewType("OGDateTime", Annotated[datetime, Timezone(DEFAULT_TIMEZONE)])
OGTimestamp = NewType("OGTimestamp", Annotated[float, Ge(0), Timezone(DEFAULT_TIMEZONE)])
OGTimeDelta = NewType("OGTimeDelta", Annotated[timedelta, Timezone(DEFAULT_TIMEZONE)])


class DateTime:
    __value: OGDateTime

    def __init__(self, value: OGDateTime) -> None:
        self.__value = value

    def __str__(self) -> str:
        return self.__value.isoformat()

    def __repr__(self):
        return self.__value.isoformat()

    @classmethod
    def now(cls, tz: tzinfo = DEFAULT_TIMEZONE) -> "DateTime":
        return DateTime(cast(OGDateTime, datetime.now(tz)))

    @classmethod
    def from_raw_datetime(cls, value: datetime) -> "DateTime":
        return DateTime(cast(OGDateTime, value.astimezone(DEFAULT_TIMEZONE)))

    @classmethod
    def from_raw_timestamp(cls, value: float) -> "DateTime":
        return DateTime(cast(OGDateTime, datetime.fromtimestamp(value, DEFAULT_TIMEZONE)))

    @classmethod
    def from_raw_string(cls, value: str) -> "DateTime":
        return DateTime(cast(OGDateTime, parser.parse(value).astimezone(DEFAULT_TIMEZONE)))

    def to_datetime(self) -> OGDateTime:
        return self.__value

    def to_timestamp(self) -> OGTimestamp:
        return cast(OGTimestamp, self.__value.timestamp())

    def to_iso_format(self) -> str:
        return self.__value.isoformat()


class TimeDelta:
    __value: OGTimeDelta

    def __init__(self, value: OGTimeDelta):
        self.__value = value

    def __str__(self) -> str:
        return self.__value.__str__()

    def __repr__(self):
        return self.__value.__repr__()

    @classmethod
    def from_raw_timedelta(cls, value: timedelta) -> "TimeDelta":
        return TimeDelta(cast(OGTimeDelta, value))

    @classmethod
    def between(cls, start: DateTime, end: DateTime) -> "TimeDelta":
        return TimeDelta(cast(OGTimeDelta, end.to_datetime() - start.to_datetime()))

    def after(self, start: DateTime) -> DateTime:
        return DateTime(start.to_datetime() + self.__value)

    def before(self, end: DateTime) -> DateTime:
        return DateTime(end.to_datetime() - self.__value)

    def to_seconds(self) -> Annotated[int, Ge(0)]:
        return int(round(self.__value.total_seconds()))
