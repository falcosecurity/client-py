import argparse

import falco

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-format", "-o", dest="output_format", default=None, help="output_format")
    args = parser.parse_args()

    c = falco.Client(
        endpoint="localhost:5060",
        client_crt="/tmp/client.crt",
        client_key="/tmp/client.key",
        ca_root="/tmp/ca.crt",
        output_format=args.output_format,
    )

    for event in c.subscribe(falco.Request(keepalive=True)):
        print(event)
