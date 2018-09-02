#!/bin/bash

echo "
group001:
  hosts:
    - host001
    - host002
  vars:
    var1: true
  children:
    - group002

group002:
  hosts:
    - host003
    - host004
  vars:
    var2: true
  children: []
"
