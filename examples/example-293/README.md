# Role UBUNTU20-CIS
upstream: https://github.com/ansible-lockdown/UBUNTU20-CIS
fork:     https://github.com/vbotka/UBUNTU20-CIS


## Clone fork

```
shell> cd /scratch
shell> git clone https://github.com/vbotka/UBUNTU20-CIS.git
```


## Execute a development branch

```
shell> (cd /scratch/vbotka.UBUNTU20-CIS/; git checkout integration_test-parse_etc_password)
Already on 'integration_test-parse_etc_password'
```

```
shell> export ANSIBLE_ROLES_PATH=/scratch/
shell> export ANSIBLE_DISPLAY_OK_HOSTS=true
shell> export ANSIBLE_DISPLAY_SKIPPED_HOSTS=true
shell> ansible-playbook pb.yml
```


## Test integration target parse_etc_password

```
shell> (cd /scratch/vbotka.UBUNTU20-CIS/; git checkout integration_test-parse_etc_password)
Already on 'integration_test-parse_etc_password'
```

```
shell> export ANSIBLE_ROLES_PATH=/scratch/vbotka.UBUNTU20-CIS/tests/integration/targets/
shell> export ANSIBLE_DISPLAY_OK_HOSTS=true
shell> export ANSIBLE_DISPLAY_SKIPPED_HOSTS=true
shell> ansible-playbook pb_itest-parse_etc_password.yml
```

```
```
