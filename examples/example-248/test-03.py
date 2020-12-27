#!/usr/bin/env python3

from collections.abc import Mapping

dict1 = {'k1': {'k11': 'v11'}, 'k2': {'k21': 'v21'}, 'k3': {'k31': 'v31'}}
keys1 = list(dict1.keys())
values1 = list(dict1.values())

lst = list(isinstance(value, Mapping) for value in values1)
print(lst)

print(any(list(isinstance(value, Mapping) for value in values1)))
print(all(list(isinstance(value, Mapping) for value in values1)))

dict2 = {'k1': {'k11': 'v11'}, 'k2': {'k21': 'v21'}, 'k3': 'k31'}
keys2 = list(dict2.keys())
values2 = list(dict2.values())

lst = list(isinstance(value, Mapping) for value in values2)
print(lst)

print(any(list(isinstance(value, Mapping) for value in values2)))
print(all(list(isinstance(value, Mapping) for value in values2)))

# > ./test-03.py
# [True, True, True]
# True
# True
# [True, True, False]
# True
# False
