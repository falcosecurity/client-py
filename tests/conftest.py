from datetime import datetime

import pytest
from dateutil import tz

from falco import OutputsRequest, OutputsResponse, VersionRequest, VersionResponse


@pytest.fixture
def outputs_request():
    return OutputsRequest()


@pytest.fixture
def outputs_response():
    return OutputsResponse(
        time=datetime(2020, 1, 1, 22, 55, 59, 300000, tz.UTC),
        priority=OutputsResponse.Priority.CRITICAL,
        source=OutputsResponse.Source.K8S_AUDIT,
        rule="rule",
        output="output",
        output_fields={"a": "b"},
        hostname="hostname",
    )


@pytest.fixture
def version_request():
    return VersionRequest()


@pytest.fixture
def version_response():
    return VersionResponse(version="123456", major=1, minor=2, patch=3, prerelease="654321", build="1337")
