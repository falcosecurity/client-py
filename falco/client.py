import grpc

from falco.client_credentials import get_grpc_channel_credentials
from falco.domain import OutputsRequest, OutputsResponse, VersionRequest, VersionResponse
from falco.errors import InvalidFormat, TLSConfigError
from falco.svc.outputs_pb2_grpc import serviceStub as outputsServiceStub
from falco.svc.version_pb2_grpc import serviceStub as versionServiceStub


class Client:
    def __init__(self, endpoint, client_crt=None, client_key=None, ca_root=None, output_format=None, *args, **kw):
        if endpoint.startswith("unix:///"):
            channel = grpc.insecure_channel(endpoint, options=[("grpc.max_receive_message_length", 1024 * 1024 * 512)],)

        else:
            if None in [client_crt, client_key, ca_root]:
                raise TLSConfigError(
                    "must provide valid paths for all of the TLS data: client certificate, client key, and CA certificate"
                )
            channel = grpc.secure_channel(
                endpoint,
                credentials=get_grpc_channel_credentials(client_crt, client_key, ca_root),
                options=[("grpc.max_receive_message_length", 1024 * 1024 * 512)],
            )

        self._outputs_client = outputsServiceStub(channel)
        self._version_client = versionServiceStub(channel)
        self.output_format = output_format

    @property
    def output_format(self):
        return self._output_format

    @output_format.setter
    def output_format(self, o):
        if o and o not in OutputsResponse.SERIALIZERS:
            raise InvalidFormat("invalid output format")
        self._output_format = o

    def sub(self):
        responses = self._outputs_client.sub(OutputsRequest.generator(with_delay=0.1))
        for pb_resp in responses:
            resp = OutputsResponse.from_proto(pb_resp)

            if self.output_format:
                yield getattr(resp, OutputsResponse.SERIALIZERS[self.output_format])()
                continue

            yield resp

    def get(self):
        responses = self._outputs_client.get(OutputsRequest().to_proto())
        for pb_resp in responses:
            resp = OutputsResponse.from_proto(pb_resp)

            if self.output_format:
                yield getattr(resp, OutputsResponse.SERIALIZERS[self.output_format])()
                continue

            yield resp

    def version(self):
        req = VersionRequest().to_proto()
        resp = VersionResponse.from_proto(self._version_client.version(req))

        if self.output_format:
            return getattr(resp, VersionResponse.SERIALIZERS[self.output_format])()

        return resp
