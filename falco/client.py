import grpc

from falco.client_credentials import get_grpc_channel_credentials
from falco.domain import Response, Request
from falco.svc.outputs_pb2_grpc import serviceStub as outputsServiceStub
from falco.svc.version_pb2_grpc import serviceStub as versionServiceStub
from falco.schema.version_pb2 import request as versionRequest
from falco.schema.outputs_pb2 import request as outputsRequest


class InvalidFormat(Exception):
    pass


class TLSConfigError(Exception):
    pass


class RequestGenerator:
    def __init__(self):
        pass

    def EmptyRequests(self):
        while True:
            yield outputsRequest()


class Client:
    def __init__(self, endpoint, client_crt=None, client_key=None, ca_root=None, output_format=None, *args, **kw):
        if endpoint.startswith("unix:///"):
            channel = grpc.insecure_channel(
                endpoint,
                options=[("grpc.max_receive_message_length", 1024 * 1024 * 512)],
            )

        else:
            if None in [client_crt, client_key, ca_root]:
                raise TLSConfigError("Error: Must provide valid paths to all of the TLS data: client certificate, client key, and CA certificate")
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
        if o and o not in Response.SERIALIZERS:
            raise InvalidFormat("invalid output format")

        self._output_format = o

    def sub(self):  # TODO: test

        requests = RequestGenerator()
        responses = self._outputs_client.sub(requests.EmptyRequests())
        for pb_resp in responses:
            resp = Response.from_proto(pb_resp)

            if self.output_format:
                yield getattr(resp, Response.SERIALIZERS[self.output_format])()
                continue

            yield resp

    def get(self):

        request = outputsRequest()
        responses = self._outputs_client.get(request)
        for pb_resp in responses:
            resp = Response.from_proto(pb_resp)

            if self.output_format:
                yield getattr(resp, Response.SERIALIZERS[self.output_format])()
                continue

            yield resp

    def version(self):

        return self._version_client.version(versionRequest())
