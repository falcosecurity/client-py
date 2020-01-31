import pytest

from falco.domain import Response
from output_pb2 import response


class TestResponse:
    @pytest.fixture
    def resp(self):
        return Response()  # TODO: add params

    def test_encode_and_decode(self, resp):
        processed = Response.from_proto(resp.to_proto())
        for field in Response.__slots__:
            assert getattr(resp, field) == getattr(processed, field)

    def test_response_to_proto(self):
        assert False  # TODO

    def test_response_from_proto(self):
        assert False  # TODO
