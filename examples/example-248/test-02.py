#!/usr/bin/env python3

from collections.abc import Mapping

dict = {'k1': {'k11': 'v11'}, 'k2': {'k21': 'v21'}, 'k3': {'k31': 'v31'}}
keys = list(dict.keys())
values = list(dict.values())

print(keys)
print(values)

lst = list(value for value in values)
print(lst)

for value in values:
    print(value)
    if isinstance(value, Mapping):
        print('OK')

# > ./test-02.py
# ['k1', 'k2', 'k3']
# [{'k11': 'v11'}, {'k21': 'v21'}, {'k31': 'v31'}]
# [{'k11': 'v11'}, {'k21': 'v21'}, {'k31': 'v31'}]
# {'k11': 'v11'}
# OK
# {'k21': 'v21'}
# OK
# {'k31': 'v31'}
# OK
