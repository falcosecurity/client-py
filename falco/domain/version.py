import json

from falco.schema.version_pb2 import request, response


class VersionRequest:
    __slots__ = ()

    @classmethod
    def from_proto(cls, pb_request):
        return cls()

    def to_proto(self):
        return request()


class VersionResponse:
    __slots__ = ("version", "major", "minor", "patch", "prerelease", "build")

    SERIALIZERS = {"json": "to_json"}

    def __init__(self, version: str, major: int, minor: int, patch: int, prerelease: str, build: str):
        self.version = version
        self.major = major
        self.minor = minor
        self.patch = patch
        self.prerelease = prerelease
        self.build = build

    def __repr__(self):
        return f"{self.__class__.__name__}(version={self.version}, major={self.major}, minor={self.minor}, patch={self.patch}, prerelease={self.prerelease}, build={self.build})"

    @classmethod
    def from_proto(cls, pb_response):
        return cls(
            version=pb_response.version,
            major=pb_response.major,
            minor=pb_response.minor,
            patch=pb_response.patch,
            prerelease=pb_response.prerelease,
            build=pb_response.build,
        )

    def to_proto(self):
        return response(
            version=self.version,
            major=self.major,
            minor=self.minor,
            patch=self.patch,
            prerelease=self.prerelease,
            build=self.build,
        )

    def to_json(self):
        return json.dumps(
            {
                "version": self.version,
                "major": self.major,
                "minor": self.minor,
                "patch": self.patch,
                "prerelease": self.prerelease,
                "build": self.build,
            }
        )
