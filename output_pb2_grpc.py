# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import output_pb2 as output__pb2


class serviceStub(object):
    """The `subscribe` service defines the RPC call
  to perform an output `request` which will lead to obtain an output `response`.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.subscribe = channel.unary_stream(
            "/falco.output.service/subscribe",
            request_serializer=output__pb2.request.SerializeToString,
            response_deserializer=output__pb2.response.FromString,
        )


class serviceServicer(object):
    """The `subscribe` service defines the RPC call
  to perform an output `request` which will lead to obtain an output `response`.
  """

    def subscribe(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "subscribe": grpc.unary_stream_rpc_method_handler(
            servicer.subscribe,
            request_deserializer=output__pb2.request.FromString,
            response_serializer=output__pb2.response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "falco.output.service", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
