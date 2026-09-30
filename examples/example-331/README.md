# Query inventory.
https://stackoverflow.com/questions/80006445/ansible-lookup-plugin-to-query-the-inventory


A: I would like to create a Lookup plugin that queries the inventory to gather
   some data on hosts and format them.

Q: It is possible to run ansible-inventory from a task. For example, given the
   inventory file *hosts*:

```sh
shell > ansible-inventory -i hosts --graph

@all:
  |--@ungrouped:
  |--@www:
  |  |--www_01
  |  |--www_02
  |  |--www_03
```

The playbook *pb.yml* gives:

```yaml
shell > ansible-playbook -i hosts pb.yml

PLAY [all] **********************************************************************************

TASK [Query inventory.] *********************************************************************
changed: [www_01 -> localhost]

TASK [Display inventory.] *******************************************************************
ok: [www_01] => 
    my_inventory:
        _meta:
            hostvars: {}
            profile: inventory_legacy
        all:
            children:
            - ungrouped
            - www
        www:
            hosts:
            - www_01
            - www_02
            - www_03

PLAY RECAP **********************************************************************************
www_01                     : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
