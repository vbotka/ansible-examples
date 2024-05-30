Filter keep_keys
================

The collection ansible.utils provides the filter keep_keys. Unfortunately:

* It is not working properly. See keep_keys doesn't exclude a key if
  the value is list. See the bug below.

* The documentation is poor. For example, it is not clear what
  "recursively" means in "Keep specific keys from a data recursively"

* There are only two examples and two tests. An example of
  "matching_parameter=regex" is missing. It is unclear whether the
  parameter target should be a list for regex. A list of regex(es)
  would be an anti-pattern.

* But, the main hurdle to fix this filter is the class
  AnsibleArgSpecValidator that is used in all
  ansible.utils/plugins. Such complexity is inefficient in a filter
  where a couple of comprehensions would do the job. The goal is to
  keep the code simple and test it properly.


Bug ansible.utils.keep_keys
---------------------------

See: [keep_keys doesn't exclude a key if the value is list. #353](https://github.com/ansible-collections/ansible.utils/issues/353)

Test the bug. Use ansible-orig.cfg

```yaml
shell> ansible-playbook pb1.yml -t r1
  ...
  r1:
  - k0: A
    k1: B
    k2:
    - 1
  - k0: A
    k1: B
    k2:
    - 2
```


Feature request community.general.keep_keys
-------------------------------------------

See: [Add filter keep_keys #8438](https://github.com/ansible-collections/community.general/issues/8438)

Test the custom filter my_keep_keys. See
plugins/filter/keep_keys.py. Use ansible-orig.cfg

```yaml
shell> ansible-playbook pb1.yml -t rq,rs,re,rl,rr
  ...
  rr:
  - k0_x0: A0
    k1_x1: B0
  - k0_x0: A1
    k1_x1: B1
```

Run integration tests to community.general.keep_keys. Use
ansible-orig.cfg

```yaml
shell> ansible-playbook pb2.yml

```


Pull request community.general.keep_keys
----------------------------------------

See: [Add filter keep_keys. Feature #8438. #8439](https://github.com/ansible-collections/community.general/pull/8439)

Run integration tests to community.general.keep_keys on the branch feature-filter-keep_keys

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
