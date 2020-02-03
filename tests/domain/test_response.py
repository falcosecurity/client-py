from datetime import datetime

import pytest

from falco.domain import Response


class TestResponse:
    @pytest.fixture
    def resp(self):
        return Response(
            time=datetime.now(),
            priority=Response.Priority.CRITICAL,
            source=Response.Source.K8S_AUDIT,
            rule="rule",
            output="output",
            output_fields={"a": "b"},
            hostname="hostname",
        )

    def test_encode_and_decode(self, resp):
        processed = Response.from_proto(resp.to_proto())
        for field in Response.__slots__:
            assert getattr(resp, field) == getattr(processed, field)
