SHELL := /bin/bash

# This builds using 'python -m grpc_tools.protoc' and not the protoc binary
# pip install grpcio grpcio-tools to install this module

PROTOS := protos/schema.proto protos/outputs.proto protos/version.proto
PROTO_URLS := https://raw.githubusercontent.com/falcosecurity/falco/master/userspace/falco/schema.proto https://raw.githubusercontent.com/falcosecurity/falco/master/userspace/falco/outputs.proto https://raw.githubusercontent.com/falcosecurity/falco/master/userspace/falco/version.proto
PROTO_SHAS := c2dc18811ca0d2d2cece539bdee02a3f79239ca8fa0c0aa279a56277605084b7 8fdd0a921d87908df2731b8b8b40ac9a51d2369bad4351db4a3ad79584deaa61 c57a8a3f37a14ca8f33ce6d26156c9348e716029bca87bf9143807a68b1f31f5

PROTO_DIRS := $(dir ${PROTOS})
PROTO_DIRS_INCLUDES := $(patsubst %/, -I %, ${PROTO_DIRS})

SCHEMA_OUT_DIR := falco/schema
GRPC_OUT_DIR := falco/svc

.PHONY: protos
protos: ${PROTOS}

# $(1): the proto path
# $(2): the proto URL
# $(3): the proto SHA256
define download_rule
$(1):
	@rm -f $(1)
	@mkdir -p ${PROTO_DIRS} ${SCHEMA_OUT_DIR} ${GRPC_OUT_DIR}
	@curl --silent -Lo $(1) $(2)
	@echo $(3) $(1) | sha256sum -c
	@sed -i '/option go_package/d' $(1)
	python -m grpc_tools.protoc -Iprotos --python_out=${SCHEMA_OUT_DIR} --grpc_python_out=${GRPC_OUT_DIR} $(1)
endef

$(foreach PROTO,$(PROTOS),\
	$(eval $(call download_rule,$(PROTO),$(firstword $(PROTO_URLS)),$(firstword $(PROTO_SHAS))))\
	$(eval PROTO_URLS := $(wordlist 2,$(words $(PROTO_URLS)),$(PROTO_URLS)))\
	$(eval PROTO_SHAS := $(wordlist 2,$(words $(PROTO_SHAS)),$(PROTO_SHAS)))\
)

.PHONY: clean
clean: ${PROTO_DIRS}
	@rm -rf $^

lint:
	isort .
	black .
	flake8

test:
	python -m tests.mock &
	pytest -vv --color=yes tests/
