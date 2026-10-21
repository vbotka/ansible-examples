Setup
=====

setup_distribution.yml
----------------------
```yaml
gather_facts: no
tasks:
  - setup:
      gather_subset: distribution
```
```yaml
  distribution_release: plucky
  distribution_version: 25.04
  distribution_major_version: 25
  distribution_file_path: /etc/os-release
  distribution_file_variety: Debian
  distribution_file_parsed: True
```

gather_facts-001.yml
--------------------
```yaml
gather_facts: yes
tasks:
  - debug:
    ...
```

service_facts.yml
-----------------
```yaml
gather_facts: no
tasks:
  - service_facts:
    ...
```

Notes
-----
* Module service_facts doesn't work with FreeBSD
  ansible/lib/ansible/modules/service_facts.py
  service_modules = (ServiceScanService, SystemctlScanService, AIXScanService, OpenBSDScanService)
* Ansible: Loop over a list of services and disable those from a list
  of unwanted services which are actually present
  https://stackoverflow.com/questions/51137660/ansible-loop-over-a-list-of-services-and-disable-those-from-a-list-of-unwanted
