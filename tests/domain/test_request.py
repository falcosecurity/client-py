import pytest
from falco import Request
from outputs_pb2 import request


class TestRequest:
    def test_encode_and_decode(self, req):
        processed = Request.from_proto(req.to_proto())
        # With nothing in __slots__ this doesn't test anything after this line
        for field in Request.__slots__:
            assert getattr(req, field) == getattr(processed, field)
