#!/bin/bash -e

shopt -s extglob

declare -A protos

protos=( ["https://raw.githubusercontent.com/falcosecurity/falco/dev/userspace/falco/schema.proto"]="a1f427c114b945d0880b55058862b74015d036aa722985ca6e5474ab4ed19f69" ["https://raw.githubusercontent.com/falcosecurity/falco/dev/userspace/falco/output.proto"]="4ce2f3e6d6ebc07a74535c4f21da73e44c6ef848ab83627b1ac987058be5ece9")

protodir=$PWD/proto

function clean () {
    rm -rf $protodir
    mkdir -p $protodir
}

function download_pb () {
    for f in "${!protos[@]}" ;do
        fout=$protodir/`basename $f`
        curl -s $f -o $fout
        if [ "${protos[$f]}" != "`sha256sum $fout | awk '{ print $1 }'`" ] ;then
            echo "checksum failed for $f"
            exit 1
        fi
    done
}

function compile () {
    # https://github.com/protocolbuffers/protobuf/issues/881
    for f in `find $protodir -type f -iname "*.proto"` ;do
        python -m grpc_tools.protoc -I=$protodir --python_out=. --grpc_python_out=. $f
    done
}

clean
download_pb
compile
