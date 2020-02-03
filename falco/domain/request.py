from falco.schema.output_pb2 import request


class Request:
    __slots__ = ("keepalive",)

    def __init__(self, keepalive=None):
        self.keepalive = keepalive

    def __repr__(self):
        return f"{self.__class__.__name__}(keepalive={self.keepalive})"

    @classmethod
    def from_proto(cls, pb_request):
        return cls(keepalive=pb_request.keepalive)

    def to_proto(self):
        return request(keepalive=self.keepalive)
