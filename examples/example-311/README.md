community.general.ansible_type
==============================

pb14.yml
--------

Given the target and data keep target keys

```yaml
    target: [key, other]
    data:
      - nm: first
        ld:
          - {key: 1, other: other1, foo: bar}
          - {key: 2, other: other2, foo: bar}
      - nm: second
        ld:
          - {key: 3, other: other3, foo: bar}
          - {key: 4, other: other4, foo: bar}
```

requested result

```yaml
  rd:
    - ld:
      - {key: 1, other: other1}
      - {key: 2, other: other2}
    - ld:
      - {key: 3, other: other3}
      - {key: 4, other: other4}
```


Simple test to select dict[list] is missing
-------------------------------------------

Explicit attribute map is used instead

```yaml
    rl: "{{ data |
            map(attribute='ld') |
            map('community.general.keep_keys', target=target) }}"
    rd: "{{ rl | map('community.general.dict_kv', 'ld' ) }}"
```

gives

```yaml
  rl | to_yaml: |-
    - - {key: 1, other: other1}
      - {key: 2, other: other2}
    - - {key: 3, other: other3}
      - {key: 4, other: other4}

  rd | to_yaml: |-
    - ld:
      - {key: 1, other: other1}
      - {key: 2, other: other2}
    - ld:
      - {key: 3, other: other3}
      - {key: 4, other: other4}
```

Filter community.general.ansible_type
-------------------------------------

```yaml
    sel: "{{ data | map('dict2items') |
             map('selectattr', 'value', 'community.general.ansible_type', 'list[dict]') |
             flatten }}"
    res: |
      {% filter from_yaml %}
      {% for i in sel %}
      {% set v = i.value|community.general.keep_keys(target=target) %}
      {% if v|select %}
      - {{ i.key }}: {{ v }}
      {% endif %}
      {% endfor %}
      {% endfilter %}
```

gives

```yaml
  sel | to_yaml: |-
    - key: ld
      value:
      - {foo: bar, key: 1, other: other1}
      - {foo: bar, key: 2, other: other2}
    - key: ld
      value:
      - {foo: bar, key: 3, other: other3}
      - {foo: bar, key: 4, other: other4}

  res | to_yaml: |-
    - ld:
      - {key: 1, other: other1}
      - {key: 2, other: other2}
    - ld:
      - {key: 3, other: other3}
      - {key: 4, other: other4}
```
