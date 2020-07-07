from falco.schema.outputs_pb2 import request


class Request:
    def __init__(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}"

    @classmethod
    def from_proto(cls):
        return cls()

    def to_proto(self):
        return request()
