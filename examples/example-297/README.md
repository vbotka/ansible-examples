# INI template

Test INI template

```yaml
shell> cat default-INI.j2
# {{ ansible_managed }}. Template: {{ template_path }}

{% for section, conf in ini|groupby('section', case_sensitive=ini_cs|d(False)) %}
[{{ section }}]
{% for i in conf %}
{{ i.line }}
{% endfor %}

{% endfor %}
```

## case_sensitive=False (default)

```yaml
    config1:
      - {section: default, line: 'key1 = val1'}
      - {section: default, line: 'key2 = val2'}
      - {section: general, line: 'key3 = val3'}
      - {section: custom, line: 'key4 = val4'}
      - {section: custom, line: 'key5 = val5'}
```
```yaml
    - debug:
        msg: "{{ lookup('template', 'default-INI.j2') }}"
      vars:
        ini: "{{ config1 }}"
```
gives
```ini
    # Ansible managed. Template: default-INI.j2
  
    [custom]
    key4 = val4
    key5 = val5
  
    [default]
    key1 = val1
    key2 = val2
  
    [general]
    key3 = val3
```

The data *config2* gives the same result with *ini_cs=False*
(default). The format of the first item will be taken.

## case_sensitive=True

```yaml
    config2:
      - {section: default, line: 'key1 = val1'}
      - {section: Default, line: 'key2 = val2'}
      - {section: general, line: 'key3 = val3'}
      - {section: custom, line: 'key4 = val4'}
      - {section: custom, line: 'key5 = val5'}
```
```yaml
    - debug:
        msg: "{{ lookup('template', 'default-INI.j2') }}"
      vars:
        ini: "{{ config1 }}"
        ini_cs: True
```
gives
```ini
    # Ansible managed. Template: default-INI.j2
  
    [Default]
    key2 = val2
  
    [custom]
    key4 = val4
    key5 = val5
  
    [default]
    key1 = val1
  
    [general]
    key3 = val3
```
