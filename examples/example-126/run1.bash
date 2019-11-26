#!/bin/bash

rcfile=private1/artifacts/ID01/rc
statusfile=private1/artifacts/ID01/status

ansible-runner -p test.yml -i ID01 run private1
rc=$(cat $rcfile)
echo "rc: $rc"

until [ "0"  == "$rc" ]; do
    ansible-runner -p test.yml -i ID01 run private1
    rc=$(cat $rcfile)
    echo "rc: $rc"
done
