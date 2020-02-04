# client-py

> Python client and SDK for Falco

## Usage

### Output subscribe

```python
import falco
client = falco.Client(endpoint="localhost:5060", client_crt="/tmp/client.crt", client_key="/tmp/client.key", ca_root="/tmp/ca.crt")
for event in client.subscribe(falco.Request(keepalive=True)):
    print(event)
```

or try it directly (make sure you have the client certificates in `/tmp`):

```
python -m examples.get_events -o json
```

### Output formats

Currently there are two output formats available: JSON and Python classes.
To change output format, pass the `output_format` to the Client object.

## Development

### Dependencies

**TBD**

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
