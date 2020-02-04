import pytest

from falco import Request
from output_pb2 import request


class TestRequest:
    def test_encode_and_decode(self, req):
        processed = Request.from_proto(req.to_proto())
        for field in Request.__slots__:
            assert getattr(req, field) == getattr(processed, field)

    @pytest.mark.parametrize("keepalive", [True, False])
    def test_request_from_proto(self, keepalive):
        pb_req = request(keepalive=keepalive)
        req = Request.from_proto(pb_req)

        assert req.keepalive == keepalive
        assert pb_req.keepalive == req.keepalive

    @pytest.mark.parametrize("keepalive", [True, False])
    def test_request_to_proto(self, keepalive):
        req = Request(keepalive=keepalive)
        pb_req = req.to_proto()

        assert pb_req.keepalive == keepalive
        assert pb_req.keepalive == req.keepalive
