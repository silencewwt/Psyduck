#!/bin/bash -ex

DIR=$(pwd)
CLIENT=${DIR}/psyduck/client/adapter.py
RESOURCES="https://www.bitmex.com/api/explorer/swagger.json"

echo "Getting swagger.json..."
rm ${DIR}/swagger.json
wget ${RESOURCES}

echo "Generating client code..."
python ${DIR}/codegen.py -o ${CLIENT} -s ${DIR}/swagger.json
yapf -i ${CLIENT}

rm ${DIR}/swagger.json
