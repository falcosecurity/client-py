from falco import VersionRequest, VersionResponse


class TestVersionRequest:
    def test_encode_and_decode(self, version_request):
        # Note: this class is empty but the test will still be valid after a schema change
        processed = VersionRequest.from_proto(version_request.to_proto())
        for field in VersionRequest.__slots__:
            assert getattr(version_request, field) == getattr(processed, field)


class TestVersionResponse:
    def test_encode_and_decode(self, version_response):
        processed = VersionResponse.from_proto(version_response.to_proto())
        for field in VersionResponse.__slots__:
            assert getattr(version_response, field) == getattr(processed, field)
