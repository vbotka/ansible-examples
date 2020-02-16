#!/bin/sh

#export ANSIBLE_STDOUT_CALLBACK=default
#export ANSIBLE_STDOUT_CALLBACK=stderr
export ANSIBLE_STDOUT_CALLBACK=actionable

# Filter plugins
ansible-playbook test-bool_filters.yml
ansible-playbook test-dict_filters.yml
ansible-playbook test-hash_filters.yml
ansible-playbook test-list_filters.yml
ansible-playbook test-version_filters.yml
ansible-playbook test-string_filters.yml
ansible-playbook test-file_filters.yml
ansible-playbook test-datetime_filters.yml
