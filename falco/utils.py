from google.protobuf.timestamp_pb2 import Timestamp


def pb_timestamp_from_datetime(dt):
    ts = Timestamp()
    ts.FromDatetime(dt)
    return ts


def load_file(filepath):
    with open(filepath, "rb") as f:
        return f.read()
