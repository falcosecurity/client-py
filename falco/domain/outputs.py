import json
import time
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Optional

from dateutil import tz

from falco.domain.common import pb_timestamp_from_datetime
from falco.schema.outputs_pb2 import request, response
from falco.schema.schema_pb2 import priority, source


class OutputsRequest:
    __slots__ = ()

    @classmethod
    def from_proto(cls, pb_request):
        return cls()

    def to_proto(self):
        return request()

    @staticmethod
    def generator(with_delay: float = 0.0, run_for: Optional[timedelta] = None):
        started_at = datetime.utcnow()
        while True:
            yield OutputsRequest().to_proto()

            if run_for is not None:
                if datetime.utcnow() - started_at > run_for:
                    return

            time.sleep(with_delay)


class OutputsResponse:
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

    PB_PRIORITY_TO_PRIORITY_MAP = {
        0: Priority.EMERGENCY,
        1: Priority.ALERT,
        2: Priority.CRITICAL,
        3: Priority.ERROR,
        4: Priority.WARNING,
        5: Priority.NOTICE,
        6: Priority.INFORMATIONAL,
        7: Priority.DEBUG,
    }

    class Source(Enum):
        SYSCALL = "syscall"
        K8S_AUDIT = "k8s_audit"

    PB_SOURCE_TO_SOURCE_MAP = {
        0: Source.SYSCALL,
        1: Source.K8S_AUDIT,
    }

    SERIALIZERS = {"json": "to_json"}

    def __init__(
        self, time=None, priority=None, source=None, rule=None, output=None, output_fields=None, hostname=None,
    ):
        self.time: datetime = time.astimezone(tz.tzutc())
        self.priority: OutputsResponse.Priority = priority
        self.source: OutputsResponse.Source = source
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
        if p and isinstance(p, OutputsResponse.Priority):
            self._priority = p

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, s):
        self._source = None
        if s and isinstance(s, OutputsResponse.Source):
            self._source = s

    @classmethod
    def from_proto(cls, pb_response):
        timestamp_dt = datetime.fromtimestamp(pb_response.time.seconds + pb_response.time.nanos / 1e9)

        return cls(
            time=timestamp_dt,
            priority=OutputsResponse.PB_PRIORITY_TO_PRIORITY_MAP[pb_response.priority],
            source=OutputsResponse.PB_SOURCE_TO_SOURCE_MAP[pb_response.source],
            rule=pb_response.rule,
            output=pb_response.output,
            output_fields=dict(pb_response.output_fields),
            hostname=pb_response.hostname,
        )

    def to_proto(self):
        return response(
            time=pb_timestamp_from_datetime(self.time),
            priority=priority.Value(self.priority.value),
            source=source.Value(self.source.value),
            rule=self.rule,
            output=self.output,
            output_fields=self.output_fields,
            hostname=self.hostname,
        )

    def to_json(self):
        return json.dumps(
            {
                "time": self.time.isoformat(),
                "priority": self.priority.value,
                "source": self.source.value,
                "rule": self.rule,
                "output": self.output,
                "output_fields": self.output_fields,
                "hostname": self.hostname,
            }
        )
