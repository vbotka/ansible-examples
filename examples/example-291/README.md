# Integration tests of Ansible filter_core


```
shell> ansible --version
ansible [core 2.12.7]
  config file = /export/ansible-examples/examples/example-291/ansible.cfg
  configured module search path = ['/export/ansible-examples/examples/example-291/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  ansible collection location = /export/ansible-examples/examples/example-291/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible
  python version = 3.8.5 (default, Jan 27 2021, 15:41:15) [GCC 9.3.0]
  jinja version = 3.0.1
  libyaml = True
```		

```
shell> (cd /scratch/vbotka.ansible; git checkout stable-2.12)
Already on 'stable-2.12'
Your branch is up to date with 'upstream/stable-2.12'.
```

```
shell> export ANSIBLE_ROLES_PATH=/scratch/vbotka.ansible/test/integration/targets/
shell> export ANSIBLE_DISPLAY_OK_HOSTS=false
shell> export ANSIBLE_DISPLAY_SKIPPED_HOSTS=false
shell> export OUTPUT_DIR=/tmp/ansible.integration
shell> ansible-playbook pb-integration-test.yml
```

```
PLAY RECAP ***********************************************************************************
localhost: ok=82   changed=4    unreachable=0    failed=0    skipped=1    rescued=0    ignored=26
```
