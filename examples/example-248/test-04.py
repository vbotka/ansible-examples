#!/usr/bin/env python3

from collections.abc import Mapping

dict2 = {'k1': {'k11': 'v11'}, 'k2': {'k21': 'v21'}, 'k3': 'k31'}
keys2 = list(dict2.keys())
values2 = list(dict2.values())

lst = list(isinstance(value, Mapping) for value in values2)
print(lst)

if any(list(isinstance(value, Mapping) for value in values2)):
    print('any OK')

if all(list(isinstance(value, Mapping) for value in values2)):
    print('all OK')

# > ./test-04.py
# [True, True, False]
# any OK
