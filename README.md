# client-py

> Python client and SDK for Falco

## Usage

### Output subscribe

```python
import falco
client = falco.Client(endpoint="localhost:5060", client_crt="/tmp/client.crt", client_key="/tmp/client.key", ca_root="/tmp/ca.crt")
for event in client.sub()):
    print(event)
```

or try it directly (make sure you have the client certificates in `/tmp` or use the unix socket address), for example:

```
python -m examples.tls_sub_events -o json
python -m examples.unixsocket_get_events -o json
python -m examples.unixsocket_get_version
```

### Output format

Currently there are two output formats available: JSON and Python classes.
To change output format, pass the `output_format` parameter to the Client object.

## Development

### Dependencies

To install development dependencies, run `pip install -r requirements-dev.txt`.

### Update protos

Perform the following edits to the Makefile:

1. Update the PROTOS array with the destination path of the .proto file.
2. Update the PROTO_URLS array with the URL from which to download it.
3. Update thr PROTO_SHAS array with the SHA256 sum of the file to download.
4. Execute the following commands:

```console
make clean
make protos
```

### Tests

To run the tests, run `make test`.

### Misc

To format the code, run `make lint`.
