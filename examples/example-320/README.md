# Jinja2 Whitespace Control

https://jinja.palletsprojects.com/en/2.10.x/templates/#whitespace-control

Quoting:

> If you add a minus sign (-) to the start or end of a block (e.g. a
  For tag), a comment, or a variable epression, the whitespaces before
  or after that block will be removed.

given the data

```yaml
    grp:
      - {length: 1, flag: x}
      - {length: 2}
      - {length: 3, flag: f}
      - {length: 4, flag: f}
```

* The simplified template from your question

```yaml
{% for m in grp %}
        {{ m.length }}
        xyz
    {% if m.flag is defined and m.flag == "f" %}
        yes f {% endif %}
    {% endfor %}
```

adds the blank lines

```
        1
        xyz
  
        2
        xyz
  
        3
        xyz
        yes f
        4
        xyz
        yes f
```

* If you use the minus sign

```yaml
    {% for m in grp %}
        {{ m.length }}
        xyz
    {% if m.flag is defined and m.flag == "f" %}
        yes f
    {% endif -%}
    {% endfor %}
```

there are no blank lines

```
        1
        xyz
        2
        xyz
        3
        xyz
        yes f
        4
        xyz
        yes f
```

* The condition can be simplified. The template below gives the same result

```yaml
    {% for m in grp %}
        {{ m.length }}
        xyz
    {% if m.flag|default('') == "f" %}
        yes f
    {% endif -%}
    {% endfor %}
```
