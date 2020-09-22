from google.protobuf.timestamp_pb2 import Timestamp


def pb_timestamp_from_datetime(dt):
    ts = Timestamp()
    ts.FromDatetime(dt)
    return ts
