from datetime import datetime

import pytest

from falco import Request, Response


@pytest.fixture
def resp():
    return Response(
        time=datetime(2020, 1, 1, 23, 55, 59, 300000),
        priority=Response.Priority.CRITICAL,
        source=Response.Source.K8S_AUDIT,
        rule="rule",
        output="output",
        output_fields={"a": "b"},
        hostname="hostname",
    )


@pytest.fixture
def req():
    return Request(keepalive=True)
