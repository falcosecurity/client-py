from falco.schema.outputs_pb2 import request


class Request:
    __slots__ = []

    @classmethod
    def from_proto(cls, pb_request):
        return cls()

    def to_proto(self):
        return request()
