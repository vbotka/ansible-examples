Filter replace_keys
===================

The collection ansible.utils provides the filter replace_keys.

Feature request community.general.replace_keys
----------------------------------------------

See: [Add filter replace_keys #8445](https://github.com/ansible-collections/community.general/issues/8445)

Test the custom filter my_replace_keys. See
plugins/filter/replace_keys.py. Use ansible-orig.cfg

```yaml
shell> ansible-playbook pb1.yml -t rq,rs,re,rl,rr

```

Run integration tests to community.general.keep_keys. Use
ansible-orig.cfg

```yaml
shell> ansible-playbook pb2.yml -e quiet_test=false

```


Pull request community.general.replace_keys
-------------------------------------------

See: [Add filter replace_keys #8446](https://github.com/ansible-collections/community.general/pull/8446)

Run integration tests to community.general.replace_keys on the branch feature-filter-replace-keys

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
shell> ansible-playbook pb-test.yml -e quiet_test=false

```
