#!/usr/bin/env python3

print(all([True, True, True]))
print(all([False, True, True]))
print(any([True, False, False]))
print(any([False, False, False]))

# > ./test-01.py
# True
# False
# True
# False
