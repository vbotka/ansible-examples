# INI template. Data in a dictionary.

Test INI template. Data in a dictionary.

```yaml
shell> cat default_dict-INI.j2
# {{ ansible_managed }}. Template: {{ template_path }}

{% set space=extra_space|d(false)|ternary(' ', '') %}
{% for section, conf in ini.items() %}
[{{ section }}]
{% for key, value in conf.items() %}
{% if value %}
{{ key }}{{ space }}={{ space }}{{ value }}
{% else %}
{{ key }}
{% endif %}
{% endfor %}

{% endfor %}
```

## No extra space (default)

```yaml
    config1:
      default:
        key1: val1
        key2: val2
      general:
        key3: val3
      custom:
        key4: val4
        key5: val5
```
```yaml
    - debug:
        msg: "{{ lookup('template', 'default_dict-INI.j2') }}"
      vars:
        ini: "{{ config1 }}"
```
gives

```ini
    # Ansible managed. Template: default_dict-INI.j2
  
    [default]
    key1=val1
    key2=val2
  
    [general]
    key3=val3
  
    [custom]
    key4=val4
    key5=val5
```

## Extra space

```yaml
    - debug:
        msg: "{{ lookup('template', 'default_dict-INI.j2') }}"
      vars:
        ini: "{{ config1 }}"
        extra_space: true
```
gives

```ini
    # Ansible managed. Template: default_dict-INI.j2
  
    [default]
    key1 = val1
    key2 = val2
  
    [general]
    key3 = val3
  
    [custom]
    key4 = val4
    key5 = val5
```

## No value is allowed

```yaml
    config2:
      default:
        key1: val1
        key2:
```
```yaml
    - debug:
        msg: "{{ lookup('template', 'default_dict-INI.j2') }}"
      vars:
        ini: "{{ config2 }}"
```
gives

```ini
    # Ansible managed. Template: default_dict-INI.j2
  
    [default]
    key1=val1
    key2
```
