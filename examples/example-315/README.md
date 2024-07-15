Debugging modules
=================
https://docs.ansible.com/ansible/latest/dev_guide/debugging.html#debugging-modules

No packages available
---------------------

```yaml
    - community.general.pkgng:
        name: "{{ item }}"
        state: latest
      loop:
        - security/py-cryptography
        - security/py-openssl
        - security/py-acme
```

```bash
shell> ansible-playbook -i hosts pb1.yml -CD

  ...

TASK [community.general.pkgng] ***********************************************************************************
changed: [ca] => (item=security/py-cryptography)
changed: [ca] => (item=security/py-openssl)
changed: [ca] => (item=security/py-acme)

```

```bash
shell> ansible-playbook -i hosts pb1.yml

  ...

TASK [community.general.pkgng] ***********************************************************************************
failed: [ca] (item=security/py-cryptography) => changed=false 
  ansible_loop_var: item
  item: security/py-cryptography
  msg: failed to upgrade security/py-cryptography
  stderr: |-
    pkg: No packages available to upgrade matching 'security/py-cryptography' have been found in the repositories
  stderr_lines: <omitted>
  stdout: |-
    Updating FreeBSD repository catalogue...
    FreeBSD repository is up to date.
    All repositories are up to date.
  stdout_lines: <omitted>
failed: [ca] (item=security/py-openssl) => changed=false

  ...
```

ANSIBLE_KEEP_REMOTE_FILES=1
---------------------------

Keep AnsiballZ on the remote host

```bash
shell> ANSIBLE_KEEP_REMOTE_FILES=1 ansible-playbook -i hosts pb2.yml

  ...

TASK [community.general.pkgng] ***********************************************************************************
fatal: [ca]: FAILED! => changed=false 
  msg: failed to upgrade security/py-cryptography
  stderr: |-
    pkg: No packages available to upgrade matching 'security/py-cryptography' have been found in the repositories
  stderr_lines: <omitted>
  stdout: |-
    Updating FreeBSD repository catalogue...
    FreeBSD repository is up to date.
    All repositories are up to date.
  stdout_lines: <omitted>
  ...
```

Login to the remote host

```bash
shell> ssh ca
shell> cd .ansible/tmp
shell> ls -1
ansible-tmp-1720871908.744144-213197-89039727748467
ansible-tmp-1720871910.605425-213210-198676557022421
shell> cd ansible-tmp-1720871910.605425-213210-198676557022421
shell> ls -1
AnsiballZ_pkgng.py
```

Unpack AnsiballZ
----------------

```bash
shell> python AnsiballZ_pkgng.py explode
Module expanded into:
/home/admin/.ansible/tmp/ansible-tmp-1720871910.605425-213210-198676557022421/debug_dir
shell> ls -1
AnsiballZ_pkgng.py
debug_dir
```

Enable pdb
----------

* https://docs.python.org/3/library/pdb.html#module-pdb

On the remote host:

* Edit the module and enable pdb

```bash
shell> emacs debug_dir/ansible_collections/community/general/plugins/modules/pkgng.py
```

Add the below line

```python
import pdb; pdb.set_trace()
```

Debug the module
----------------

```bash
shell> python3.11 AnsiballZ_pkgng.py execute
```
