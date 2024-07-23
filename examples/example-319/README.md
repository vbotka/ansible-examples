# Filter basename

```yaml
  files: "{{ query('fileglob', '/tmp/ansible/files/*') }}"
  names: "{{ files | map('basename') | map('splitext') | map('first') }}"
```

gives

```yaml
  files:
  - /tmp/ansible/files/admin.txt
  - /tmp/ansible/files/www.txt
  - /tmp/ansible/files/bob.txt

  names:
  - admin
  - www
  - bob
```
  
