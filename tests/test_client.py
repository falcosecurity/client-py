import pytest

from falco import Client
from tests.mock import MOCK_ADDRESS


class TestClient:
    @pytest.fixture
    def client(self):
        return Client(MOCK_ADDRESS)

    def test_client_get_version(self, client):
        version = client.version()

        assert version.version == "123456"
        assert version.major == 1
        assert version.minor == 2
        assert version.patch == 3
        assert version.prerelease == "654321"
        assert version.build == "1337"

    def test_client_get_outputs(self, client):
        for ev in client.get():
            assert ev.output in {"1", "2", "3"}

    def test_client_sub_outputs(self, client):
        for ev in client.sub():
            assert ev.output in {"1", "2", "3"}
