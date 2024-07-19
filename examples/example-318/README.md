# lookup plugin pipe


```yaml
    - set_fact:
        needrestart: "{{ lookup('pipe', cmd) | from_yaml }}"
      vars:
        cmd: cat needrestart.txt
```

gives

```yaml
  needrestart:
    NEEDRESTART-KCUR: 5.14.0-362.24.1.el9_3.0.1.x86_64
    NEEDRESTART-KEXP: 5.14.0-362.24.1.el9_3.0.1.x86_64
    NEEDRESTART-KSTA: 2
    NEEDRESTART-UCSTA: 0
    NEEDRESTART-VER: 3.6
``
