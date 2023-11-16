# Ansible test fqdn_valid

Synopsis: Test validity of hostname

Requires: https://pypi.org/project/fqdn/

> Validates fully-qualified domain names against RFC 1123, so that
  they are acceptable to modern browsers

Source: https://github.com/ypcrts/fqdn


## Reference implementation fqdn_test.py

```bash
fqdn_test <hostname> [min_labels] [allow_underscores]
default:
min_labels=1
allow_underscores=False
```

```bash
shell> ./fqdn_test.py srv.example.com
is_valid: True
absolute: srv.example.com.
is_valid_absolute: False
is_valid_relative: True
labels_count: 3
relative: srv.example.com
```

```bash
shell> ./fqdn_test.py -srv
invalid FQDN -srv
```

## Ansible test fqdn_valid

* See: test_plugins/fqdn_valid.py
* See and run: pb.yml


### min_labels=1, allow_underscores=False

```
srv.example.com True
9rv.example.com True
-rv.example.com False
srv True
9rv True
-rv False
s_v False
```

### min_labels=1, allow_underscores=True

```
9rv True
-rv False
s_v True
```

### min_labels=2, allow_underscores=True

```
9rv False
srv.x True
s_v.x.y True
s_v-.x.y False
```
