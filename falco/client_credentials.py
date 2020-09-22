import grpc


def load_file(filepath):
    with open(filepath, "rb") as f:
        return f.read()


def get_grpc_channel_credentials(client_crt, client_key, ca_root):
    """Returns a ChannelCredentials object to use with the grpc channel

    https://grpc.github.io/grpc/python/grpc.html#create-client-credentials
    """

    root_certificates = load_file(ca_root)
    private_key = load_file(client_key)
    certificate_chain = load_file(client_crt)

    return grpc.ssl_channel_credentials(
        root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain,
    )
