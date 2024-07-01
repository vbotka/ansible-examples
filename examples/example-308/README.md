Python method keys()
====================

https://stackoverflow.com/questions/31468300/python-dictionary-keys-method
https://stackoverflow.com/questions/61095210/ansible-how-to-create-list-of-dictionary-keys

pb1.yml
-------

Some filters convert a dictionary when used as an argument where a
list is expected, to the list of its keys. For example, the filter
*difference* manipulates lists

```yaml
years: "{{ deploy_env.dev.schemas.keys() | list }}"
reslt: "{{ deploy_env.dev.schemas | difference(['year2']) }}"
```

pb2.yml
-------

The method key() is redundant in the above expression. By default, a
dictionary conversion to a list returns the list of the dictionary's
keys. For example, the below iteration gives the same result

```yaml
      loop: "{{ deploy_env.dev.schemas | list }}"
```
