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
    __slots__ = (
        "version",
        "major",
        "minor",
        "patch",
        "prerelease",
        "build",
        "engine_version",
        "engine_fields_checksum",
    )

    SERIALIZERS = {"json": "to_json"}

    def __init__(
        self,
        version: str,
        major: int,
        minor: int,
        patch: int,
        prerelease: str,
        build: str,
        engine_version: int,
        engine_fields_checksum: str,
    ):
        self.version = version
        self.major = major
        self.minor = minor
        self.patch = patch
        self.prerelease = prerelease
        self.build = build
        self.engine_version = engine_version
        self.engine_fields_checksum = engine_fields_checksum

    def __repr__(self):
        return f"{self.__class__.__name__}(version={self.version}, major={self.major}, minor={self.minor}, patch={self.patch}, prerelease={self.prerelease}, build={self.build}, engine_version={self.engine_version}, engine_fields_checksum={self.engine_fields_checksum})"

    @classmethod
    def from_proto(cls, pb_response):
        return cls(
            version=pb_response.version,
            major=pb_response.major,
            minor=pb_response.minor,
            patch=pb_response.patch,
            prerelease=pb_response.prerelease,
            build=pb_response.build,
            engine_version=pb_response.engine_version,
            engine_fields_checksum=pb_response.engine_fields_checksum,
        )

    def to_proto(self):
        return response(
            version=self.version,
            major=self.major,
            minor=self.minor,
            patch=self.patch,
            prerelease=self.prerelease,
            build=self.build,
            engine_version=self.engine_version,
            engine_fields_checksum=self.engine_fields_checksum,
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
                "engine_version": self.engine_version,
                "engine_fields_checksum": self.engine_fields_checksum,
            }
        )
