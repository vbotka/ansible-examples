#!/bin/bash
ansible-playbook test-include_dir2.yml > /scratch/tmp/dir2.log &
ansible-playbook test-include_dir.yml > /scratch/tmp/dir.log &
