Lazy evaluation
===============
https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Lazy-Evaluation

> In general, Ansible evaluates any variables in playbook content at
  the last possible second, which means that if you define a data
  structure that data structure itself can define variable values
  within it, and everything “just works” as you would expect. This
  also means variable strings can include other variables inside of
  those strings.

pb1.yml
-------

Why does ansible reevaluate a variable on each access
https://serverfault.com/a/1162434/382981

```yaml
    - set_fact:
        var1: "{{ var1 }}"
    - debug:
        var: hostvars.localhost.var1

    - debug: msg="{{ var1 }}"
    - debug: msg="{{ var1 }}"
    - debug: msg="{{ var1 }}"
```

This will create ("instantiate") hostvars.localhost.var1. Afterward,
the instantiated hostvar will be used

```yaml
  hostvars.localhost.var1: '15550984'
  msg: '15550984'
  msg: '15550984'
  msg: '15550984'
```
