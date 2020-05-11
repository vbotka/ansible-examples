#!/bin/bash
export ANSIBLE_STDOUT_CALLBACK=null
for i in {1..10}; do
    ansible-playbook pb.yml 2>/dev/null
    no_lines=`cat test-file | wc -l`
    [ $no_lines -ne 2 ] && echo "ERROR File 2 lines missing"
    cat /dev/null > test-file
    no_lines=`cat test-file | wc -l`
    [ $no_lines -ne 0 ] && echo "ERROR File not empty"
done

# shell> cat pb.yml
# - hosts:
#     - test_01
#     - test_02
#   gather_facts: false
#   tasks:
#     - lineinfile:
#         path: test-file
#         line: "{{ inventory_hostname }}"
#       delegate_to: localhost
