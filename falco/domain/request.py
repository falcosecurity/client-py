from falco.schema.outputs_pb2 import request


class Request:

    @classmethod
    def from_proto(cls, pb_request):
        return cls()

    def to_proto(self):
        return request()
