#!/usr/bin/env python
import json
my_hosts = { "all": {
                 "hosts": "18.66.1.28:",
                 "children": {
                     "stage": {
                         "hosts": "18.66.1.28:"
           }}}}
print json.dumps(my_hosts)
