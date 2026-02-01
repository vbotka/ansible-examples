# check_mode

[check_mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html)

To force a task to run in normal mode and make changes to the system,
even when the playbook is called with --check, set **check_mode: false**.


```bash
shell> ansible-playbook pb1.yml
...
ok: [localhost] => 
    ansible_check_mode: false
...
ok: [localhost] => 
    ansible_facts.getent_passwd.keys():
    - root
    - daemon
    - bin
	  ...
```

```bash
shell> ansible-playbook pb1.yml --check
...
ok: [localhost] => 
    ansible_check_mode: true
...
ok: [localhost] => 
    ansible_facts.getent_passwd.keys():
    - root
    - daemon
    - bin
	  ...
```
