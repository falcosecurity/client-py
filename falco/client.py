import grpc

from falco.domain import Response
from output_pb2_grpc import serviceStub


class Client:
    def __init__(self, grpc_endpoint, *args, **kw):
        self._client = serviceStub(
            grpc.insecure_channel(
                grpc_endpoint,
                options=[("grpc.max_receive_message_length", 1024 * 1024 * 512)],
            ),  # TODO: tls?
        )

    def subscribe(self, request):  # TODO: test
        pb_req = request.to_proto()

        for pb_resp in self._client.subscribe(pb_req):
            yield Response.from_proto(pb_resp)
