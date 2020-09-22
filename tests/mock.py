import time
from concurrent import futures
from datetime import datetime

import grpc
from dateutil import tz

from falco import OutputsResponse, VersionResponse
from falco.svc.outputs_pb2_grpc import add_serviceServicer_to_server as AddOutputsServiceServicerToServer
from falco.svc.version_pb2_grpc import add_serviceServicer_to_server as AddVersionServiceServicerToServer

MOCK_ADDRESS = "unix:///tmp/falcomock.sock"


class FalcoOutputsServicer:
    def __init__(self):
        self.events = [
            OutputsResponse(
                time=datetime(2020, 1, 1, 22, 55, 59, 300000, tz.UTC),
                priority=OutputsResponse.Priority.CRITICAL,
                source=OutputsResponse.Source.K8S_AUDIT,
                rule="rule",
                output="1",
                output_fields={"a": "b"},
                hostname="hostname",
            ),
            OutputsResponse(
                time=datetime(2020, 1, 1, 22, 55, 59, 300000, tz.UTC),
                priority=OutputsResponse.Priority.CRITICAL,
                source=OutputsResponse.Source.K8S_AUDIT,
                rule="rule",
                output="2",
                output_fields={"a": "b"},
                hostname="hostname",
            ),
            OutputsResponse(
                time=datetime(2020, 1, 1, 22, 55, 59, 300000, tz.UTC),
                priority=OutputsResponse.Priority.CRITICAL,
                source=OutputsResponse.Source.K8S_AUDIT,
                rule="rule",
                output="3",
                output_fields={"a": "b"},
                hostname="hostname",
            ),
        ]

    def get(self, request, context):
        for ev in self.events:
            yield ev.to_proto()

    def sub(self, request, context):
        for ev in self.events:
            yield ev.to_proto()


class FalcoVersionServicer:
    def version(self, request, context):
        return VersionResponse(
            version="123456", major=1, minor=2, patch=3, prerelease="654321", build="1337"
        ).to_proto()


if __name__ == "__main__":
    outputs_servicer = FalcoOutputsServicer()
    version_servicer = FalcoVersionServicer()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    AddOutputsServiceServicerToServer(outputs_servicer, server)
    AddVersionServiceServicerToServer(version_servicer, server)

    server.add_insecure_port(MOCK_ADDRESS)

    server.start()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)
