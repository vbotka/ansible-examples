#!/usr/bin/bash

trap "echo Trap!" SIGINT SIGTERM
echo "pid is $$"

while :
do
    sleep 1
done
