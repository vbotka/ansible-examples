#!/usr/bin/python3.10

import sys
from fqdn import FQDN

if len(sys.argv) == 1:
    print('fqdn_test <hostname> [min_labels] [allow_underscores]')
    exit(-1)

name = sys.argv[1]
min_labels = sys.argv[2] if len(sys.argv) > 2 else 1
allow_underscores = sys.argv[3] if len(sys.argv) > 3 else False

f = FQDN(name,
         min_labels=int(min_labels),
         allow_underscores=allow_underscores)

# for attr in dir(f):
#    print(f"{attr}: {getattr(f, attr)}")

if f.is_valid:
    print('is_valid: %s' % f.is_valid)
    print('absolute: %s' % f.absolute)
    print('is_valid_absolute: %s' % f.is_valid_absolute)
    print('is_valid_relative: %s' % f.is_valid_relative)
    print('labels_count: %s' % f.labels_count)
    print('relative: %s' % f.relative)
    exit(0)
else:
    print('invalid FQDN %s' % name)
    exit(-1)
