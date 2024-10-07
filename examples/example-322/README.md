# Test subset

```bash
shell> ansible-doc -t test -l | grep subset
ansible.builtin.issubset        is the list a subset of this other list
ansible.builtin.subset          is the list a subset of this other list
```

Both `subset` and `issubset` give the same result


```bash
shell> ansible-playbook pb1.yml
  ...
  result | to_yaml: |-
    - name: bar
      roles: [member, read]
    - name: baz
      roles: [member, update]
```
