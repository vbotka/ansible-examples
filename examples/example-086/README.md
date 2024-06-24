# hosts


## host-01 duplicate entries in inventory. Debug inventory_hostname

```sh
shell> cat hosts-01
a.example.com ansible_host=192.168.8.167
b.example.com ansible_host=192.168.8.167
b.example.com ansible_host=192.168.8.167
```
```sh
shell> ansible-inventory -i hosts-01 --list --yaml
all:
  children:
    ungrouped:
      hosts:
        a.example.com:
          ansible_host: 192.168.8.167
        b.example.com:
          ansible_host: 192.168.8.167
```
```yaml
shell> cat play10.yml 
- hosts: all
  gather_facts: false
  tasks:
    - debug:
        var: inventory_hostname
```
```yaml
shell> ansible-playbook -i hosts-01 play10.yml
  ...
ok: [a.example.com] => 
  inventory_hostname: a.example.com
ok: [b.example.com] => 
  inventory_hostname: b.example.com
```


## host-02 duplicate entries in inventory. Debug command hostname.

```sh
shell> cat hosts-02 
a.example.com ansible_host=10.1.0.51
b.example.com ansible_host=10.1.0.51
```
```sh
shell> cat play11.yml
- hosts: all
  gather_facts: false
  remote_user: admin
  tasks:
    - debug:
        var: inventory_hostname
    - command: hostname
      register: out
    - debug:
        var: out.stdout
```
```yaml
shell> ansible-playbook -i hosts-02 play11.yml
  ...
ok: [a.example.com] => 
  out.stdout: test_01
ok: [b.example.com] => 
  out.stdout: test_01
```

## ERR ansible_host not unique.

```yaml
shell> > cat play12.yml
- hosts: all
  gather_facts: false

  pre_tasks:

  ...

    - assert:
        that: groups.all|length == ansible_hosts|unique|length
        fail_msg: ERR ansible_host not unique.
      vars:
        ansible_hosts: "{{ groups.all | map('extract', hostvars, 'ansible_host') }}"
      run_once: true
	  
  ...
```

```yaml
shell> ansible-playbook -i hosts-02 play12.yml

  ...

fatal: [a.example.com]: FAILED! => changed=false 
  assertion: groups.all|length == ansible_hosts|unique|length
  evaluated_to: false
  msg: ERR ansible_host not unique.
  
  ...
```

# EOF
