Callback community.general.log_plays
====================================

```
(env) > ansible-playbook test.yml
```

```yaml
PLAY [Play 1.] *****************************************************************

TASK [debug] *******************************************************************
ok: [test_11] => 
    msg: Play 1 passed.
ok: [test_12] => 
    msg: Play 1 passed.
ok: [test_13] => 
    msg: Play 1 passed.

PLAY [Play 2.] *****************************************************************

TASK [debug] *******************************************************************
ok: [test_11] => 
    msg: Play 2 passed.
ok: [test_12] => 
    msg: Play 2 passed.
ok: [test_13] => 
    msg: Play 2 passed.

PLAY [Play 3.] *****************************************************************

TASK [debug] *******************************************************************
ok: [test_11] => 
    msg: Play 3 passed
ok: [test_12] => 
    msg: Play 3 passed
ok: [test_13] => 
    msg: Play 3 passed

PLAY RECAP *********************************************************************
test_11                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
test_12                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
test_13                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
```
shell> tree /tmp/log/
/tmp/log/
└── ansible_hosts
    ├── test_11
    ├── test_12
    └── test_13

2 directories, 3 files
```

```
shell> cat /tmp/log/ansible_hosts/test_11
Oct 21 2026 12:24:52 - test.yml -  - debug - OK - {"changed": false, "msg": "Play 1 passed.", "_ansible_verbose_always": true}
Oct 21 2026 12:24:52 - test.yml -  - debug - OK - {"changed": false, "msg": "Play 2 passed.", "_ansible_verbose_always": true}
Oct 21 2026 12:24:52 - test.yml -  - debug - OK - {"changed": false, "msg": "Play 3 passed", "_ansible_verbose_always": true}
```
