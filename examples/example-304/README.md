Filter remove_keys
==================

The collection ansible.utils provides the filter remove_keys.


Bug ansible.utils.remove_keys
-----------------------------

See: [remove_keys filter remove empty string from list #247](https://github.com/ansible-collections/ansible.utils/issues/247)

Test the bug. Use ansible-orig.cfg

```yaml
shell> ansible-playbook pb1.yml -t r1
  ...
  r1:
  - k2: []
    k3: foo
  - k2: []
    k3: bar
```


Feature request community.general.remove_keys
---------------------------------------------

See: [Add filter remove_keys #8442](https://github.com/ansible-collections/community.general/issues/8442)

Test the custom filter my_remove_keys. See
plugins/filter/remove_keys.py. Use ansible-orig.cfg

```yaml
shell> ansible-playbook pb1.yml -t rq,rs,re,rl,rr
  ...
  rr:
  - k2_x2:
    - C0
    k3_x3: foo
  - k2_x2:
    - C1
    k3_x3: bar
```

Run integration tests to community.general.keep_keys. Use
ansible-orig.cfg

```yaml
shell> ansible-playbook pb2.yml

```


Pull request community.general.remove_keys
------------------------------------------

See: [Add filter remove_keys #8443](https://github.com/ansible-collections/community.general/pull/8443)

Run integration tests to community.general.remove_keys on the branch feature-filter-remove-keys

```bash
shell> git remote -v
origin	https://github.com/vbotka/community.general.git (fetch)
origin	https://github.com/vbotka/community.general.git (push)
upstream	https://github.com/ansible-collections/community.general.git (fetch)
upstream	https://github.com/ansible-collections/community.general.git (push)
```

See ansible-test.cfg as a hint. Fit roles_path and collections_path to
your needs.

```yaml
shell> ansible-playbook pb-test.yml

```
