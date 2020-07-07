import grpc

from falco.client_credentials import get_grpc_channel_credentials
from falco.domain import Response
from falco.svc.outputs_pb2_grpc import serviceStub


class InvalidFormat(Exception):
    pass

class TLSConfigError(Exception):
    print(Exception)


class Client:
    def __init__(self, endpoint, client_crt=None, client_key=None, ca_root=None, output_format=None, *args, **kw):
        if endpoint.startswith("unix:///"):
            self._client = serviceStub(
                grpc.insecure_channel(
                    endpoint,
                    options=[("grpc.max_receive_message_length", 1024 * 1024 * 512)],
                ),
            )
            self.output_format = output_format

        else:
            if None in [client_crt, client_key, ca_root]:
                raise TLSConfigError("Error: Must provide valid paths to all of the TLS data: client certificate, client key, and CA certificate")
            self._client = serviceStub(
                grpc.secure_channel(
                    endpoint,
                    credentials=get_grpc_channel_credentials(client_crt, client_key, ca_root),
                    options=[("grpc.max_receive_message_length", 1024 * 1024 * 512)],
                ),
            )
            self.output_format = output_format

    @property
    def output_format(self):
        return self._output_format

    @output_format.setter
    def output_format(self, o):
        if o and o not in Response.SERIALIZERS:
            raise InvalidFormat("invalid output format")

        self._output_format = o

    def subscribe(self, request):  # TODO: test
        pb_req = request.to_proto()

        for pb_resp in self._client.get(pb_req):
            resp = Response.from_proto(pb_resp)

            if self.output_format:
                yield getattr(resp, Response.SERIALIZERS[self.output_format])()
                continue

            yield resp
