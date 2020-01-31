from datetime import datetime
from enum import Enum
from typing import Dict

from falco.utils import pb_timestamp_from_datetime
from output_pb2 import response


class Response:
    __slots__ = (
        "time",
        "_priority",
        "_source",
        "rule",
        "output",
        "output_fields",
        "hostname",
    )

    class Priority(Enum):
        EMERGENCY = "emergency"
        ALERT = "alert"
        CRITICAL = "critical"
        ERROR = "error"
        WARNING = "warning"
        NOTICE = "notice"
        INFORMATIONAL = "informational"
        DEBUG = "debug"

    class Source(Enum):
        SYSCALL = "syscall"
        K8S_AUDIT = "k8s_audit"

    def __init__(
        self,
        time=None,
        priority=None,
        source=None,
        rule=None,
        output=None,
        output_fields=None,
        hostname=None,
    ):
        self.time: datetime = time
        self.priority: Response.Priority = priority
        self.source: Response.Source = source
        self.rule: str = rule
        self.output: str = output
        self.output_fields: Dict = output_fields
        self.hostname: str = hostname

    def __repr__(self):
        return f"{self.__class__.__name__}(time={self.time}, priority={self.priority}, source={self.source}, rule={self.rule}, output={self.output}, output_fields={self.output_fields}, hostname={self.hostname})"

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, p):
        self._priority = None
        if p and isinstance(p, Response.Priority):
            self._priority = p

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, s):
        self._source = None
        if s and isinstance(s, Response.Source):
            self._source = s

    @classmethod
    def from_proto(cls, pb_response):
        timestamp_dt = datetime.fromtimestamp(
            pb_response.seconds + pb_response.nanos / 1e9
        )

        return cls(
            time=timestamp_dt,
            priority=Response.Priority(pb_response.priority.lower()),
            source=Response.Priority(pb_response.source.lower()),
            rule=pb_response.rule,
            output=pb_response.output,
            output_fields=pb_response.output_fields,  # TODO: this field won't work, fixme
            hostname=pb_response.hostname,
        )

    def to_proto(self):
        return response(
            time=pb_timestamp_from_datetime(self.time),
            priority=response.priority.Value(self.priority.value),
            source=response.source.Value(self.source.value),
            rule=self.rule,
            output=self.output,
            output_fields=self.output_fields,
            hostname=self.hostname,
        )
