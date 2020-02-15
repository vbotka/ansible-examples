#!/bin/sh
cat $1 | jq ".ansible_facts.packages.$2 | .[].version"
