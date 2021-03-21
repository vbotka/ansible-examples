#!/usr/bin/env python3

from sys import argv
import subprocess


def sample(host):
    cmd = ["ansible-playbook",
           "-i {},".format(host),
           "sample3.yml"]
    process = subprocess.run(cmd, capture_output=True)
    return process.stdout


def main():
    script, hostname = argv
    output = sample(hostname)
    print(output)


if __name__ == '__main__':
    main()

# shell> ./sample3.py test_11
