import grpc

from falco.client_credentials import get_grpc_channel_credentials
from falco.domain import Response
from output_pb2_grpc import serviceStub


class Client:
    def __init__(self, grpc_endpoint, client_crt, client_key, ca_root, *args, **kw):
        self._client = serviceStub(
            grpc.secure_channel(
                grpc_endpoint,
                credentials=get_grpc_channel_credentials(
                    client_crt, client_key, ca_root
                ),
                options=[("grpc.max_receive_message_length", 1024 * 1024 * 512)],
            ),
        )

    def subscribe(self, request):  # TODO: test
        pb_req = request.to_proto()

        for pb_resp in self._client.subscribe(pb_req):
            yield Response.from_proto(pb_resp)
