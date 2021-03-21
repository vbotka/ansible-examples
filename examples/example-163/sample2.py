#!/usr/bin/env python3

from sys import argv
import subprocess


def sample(host, user):
    cmd = ["ansible-playbook",
           "-i {},".format(host),
           "-e ansible_user={}".format(user),
           "sample.yml",
           "-v"]
    process = subprocess.run(cmd, capture_output=True)
    return process.stdout


def main():
    script, hostname, user = argv
    output = sample(hostname, user)
    print(output)


if __name__ == '__main__':
    main()

# shell> ./sample2.py test_11 admin
