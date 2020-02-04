import json

from falco import Response


class TestResponse:
    def test_encode_and_decode(self, resp):
        processed = Response.from_proto(resp.to_proto())
        for field in Response.__slots__:
            assert getattr(resp, field) == getattr(processed, field)

    def test_to_json(self, resp):
        assert json.loads(resp.to_json()) == {
            "hostname": "hostname",
            "output": "output",
            "output_fields": {"a": "b"},
            "priority": "critical",
            "rule": "rule",
            "source": "k8s_audit",
            "time": "2020-01-01T22:55:59.300000+00:00",
        }
