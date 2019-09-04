#!/bin/sh

my_host="$(ansible-inventory --list | jq '._meta.hostvars | to_entries[] | select (.value.ansible_host=="'"$1"'") | .key')"
my_host="$(echo $my_host | sed -e 's/^"//' -e 's/"$//')"
printf $my_host
# echo host: $my_host
# ansible-playbook -l $my_host play1.yml
