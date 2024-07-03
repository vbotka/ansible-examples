community.general.keep_keys
===========================

pb1.yml
-------

Simple test to select dict[list] is missing. Explicit attribute map
is used instead

```yaml
    data:
      - m: first
        n:
          - {x: 10, y: 11, z: 12}
          - {x: 20, y: 21, z: 22}
      - m: second
        n:
          - {x: 30, y: 31, z: 32}
          - {x: 40, y: 41, z: 33}
```

```yaml
    rl: "{{ data |
            map(attribute='n') |
            map('community.general.keep_keys', target=t) }}"
    rd: "{{ rl | map('community.general.dict_kv', 'n' ) }}"
```
