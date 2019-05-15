#!/bin/bash
hosts_file=$1
sections=$(cat $hosts_file | grep "\[" | tr -d "[]" | sort)
for i in $sections; do
    sed -n -e "/\[$i\]/,/\[/p" $hosts_file | sed '${/\[.*/d}'
done

# Is there a way to sort the groups in an ansible host file without
# sorting the hosts within the groups?
# https://stackoverflow.com/questions/56034461/is-there-a-way-to-sort-the-groups-in-an-ansible-host-file-without-sorting-the-ho

# EOF
