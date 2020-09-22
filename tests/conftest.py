from datetime import datetime

from dateutil import tz

import pytest
from falco import Request, Response


@pytest.fixture
def resp():
    return Response(
        time=datetime(2020, 1, 1, 22, 55, 59, 300000, tz.UTC),
        priority=Response.Priority.CRITICAL,
        source=Response.Source.K8S_AUDIT,
        rule="rule",
        output="output",
        output_fields={"a": "b"},
        hostname="hostname",
    )


@pytest.fixture
def req():
    return Request()
