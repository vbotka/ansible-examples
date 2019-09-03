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
    
# > python3 sample.py test_01 admin
# Using /export/home/vlado.config/.ansible/ansible-examples/examples/example-163/ansible.cfg as config file
# 
# PLAY [all] ****************************************************************************************
# 
# TASK [Gathering Facts] ****************************************************************************
# ok: [test_01]
# 
# TASK [debug] **************************************************************************************
# ok: [test_01] => {
#     "msg": "I'm on test_01"
# }
# 
# PLAY RECAP ****************************************************************************************
# test_01: ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
