# Integration tests of ansible.utils.*_keys

* ansible.utils.keep_keys
* ansible.utils.remove_keys
* ansible.utils.replace_keys


## PR

* [replace_keys: Add complex integration tests. #200](https://github.com/ansible-collections/ansible.utils/pull/200)


## Documentation

* https://github.com/ansible-collections/ansible.utils#filter-plugins
* https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.keep_keys_filter.rst
* https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.remove_keys_filter.rst
* https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.replace_keys_filter.rst


## Integration

* https://github.com/ansible-collections/ansible.utils/tree/main/tests/integration/targets/utils_keep_keys
* https://github.com/ansible-collections/ansible.utils/tree/main/tests/integration/targets/utils_remove_keys
* https://github.com/ansible-collections/ansible.utils/tree/main/tests/integration/targets/utils_replace_keys


## Best practice

There is no output if all tests passed

```
shell> export ANSIBLE_DISPLAY_OK_HOSTS=false
shell> export ANSIBLE_DISPLAY_SKIPPED_HOSTS=false
shell> ansible-playbook pb.yml

PLAY [keep keys, replace keys, remove keys] *********************************************

PLAY RECAP ******************************************************************************
localhost: ok=23   changed=0    unreachable=0    failed=0    skipped=23   rescued=0    ignored=0
```
