ansible.builtin.constructed inventory plugin
============================================

build groups based on hosts and host-variables
https://groups.google.com/g/ansible-project/c/I2J5Sno91Ss

Project
-------

```bash
shell> tree .
.
├── ansible.cfg
├── inventory
│   └── alllinux
│       ├── 01-hosts.yml
│       └── 02-constructed.yml
├── playbook_01.yml
├── playbook_02.yml
```

Create a dictionary with the lists of the allowed hosts
-------------------------------------------------------

```yaml
shell> cat inventory/alllinux/01-hosts.yml 
alllinux:
  hosts:
    test_01:
    test_02:
    test_03:
  vars:
    play_allow:
      default: []
      playbook_01: [test_01, test_02]
      playbook_02: [test_02, test_03]
```

The below playbook shall run on the hosts test_01 and test_02 only

```yaml
shell> cat playbook_01.yml
- name: playbook_01
  hosts: my_hosts
  tasks:
    - debug:
        msg: Start play
```

Use the inventory plugin *constructed* and create the group *my_hosts*
----------------------------------------------------------------------

```yaml
shell> cat inventory/alllinux/02-constructed.yml 
plugin: ansible.builtin.constructed
use_extra_vars: true
use_vars_plugins: true
compose:
  my_hosts_allow: play_allow[my_play|d('default')]
groups:
  my_hosts: inventory_hostname in my_hosts_allow
```

Run the play
------------

Unfortunately, the name of the playbook is not available
in the inventory plugins. Therefor, you have to provide
it explicitly. For example, in the extra vars *my_play*

```bash
shell> ansible-playbook -i inventory/alllinux -e my_play=playbook_01 playbook_01.yml
```

gives abridged

```yaml
ok: [test_01] =>
msg: Start play
ok: [test_02] =>
msg: Start play
```
