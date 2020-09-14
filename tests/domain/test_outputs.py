import json
from datetime import timedelta

from falco import OutputsRequest, OutputsResponse


class TestOutputsRequest:
    def test_encode_and_decode(self, outputs_request):
        # Note: this class is empty but the test will still be valid after a schema change
        processed = OutputsRequest.from_proto(outputs_request.to_proto())
        for field in OutputsRequest.__slots__:
            assert getattr(outputs_request, field) == getattr(processed, field)

    def test_generator(self):
        requests = OutputsRequest.generator(with_delay=0.2, run_for=timedelta(seconds=1))
        result_len = len(list(requests))
        assert result_len >= 2 and result_len <= 6


class TestOutputsResponse:
    def test_encode_and_decode(self, outputs_response):
        processed = OutputsResponse.from_proto(outputs_response.to_proto())
        for field in OutputsResponse.__slots__:
            assert getattr(outputs_response, field) == getattr(processed, field)

    def test_to_json(self, outputs_response):
        assert json.loads(outputs_response.to_json()) == {
            "hostname": "hostname",
            "output": "output",
            "output_fields": {"a": "b"},
            "priority": "critical",
            "rule": "rule",
            "source": "k8s_audit",
            "time": "2020-01-01T22:55:59.300000+00:00",
        }
