#!/usr/bin/env python3

from sys import argv
import subprocess


def sample(host, user):
    cmd = ["ansible-playbook",
           "-i {},".format(host),
           "-e ansible_user={}".format(user),
           "sample.yml",
           "-v"]
    subprocess.run(cmd)


def main():
    script, hostname, user = argv
    sample(hostname, user)


if __name__ == '__main__':
    main()

# How to run ansible playbooks with subprocess
# https://stackoverflow.com/questions/57763068/how-to-run-ansible-playbooks-with-subprocess/
#     
# shell> ./sample1.py test_11 admin
# 
# PLAY [all] ***********************************************************************************
# 
# TASK [Gathering Facts] ***********************************************************************
# ok: [test_11]
# 
# TASK [debug] *********************************************************************************
# ok: [test_11] =>
#   msg: I'm on test_11
# 
# PLAY RECAP ***********************************************************************************
# test_11: ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
