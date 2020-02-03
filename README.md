# client-py

> Python client and SDK for Falco

## Usage

### Output subscribe

```python
import falco
client = falco.Client(grpc_endpoint="localhost:5060", client_crt="/tmp/client.crt", client_key="/tmp/client.key", ca_root="/tmp/ca.crt")
for event in client.subscribe(falco.Request(keepalive=True)):
    print(event)
```

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
