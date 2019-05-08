#!/bin/bash
hosts_file=$1
sections=$(cat $hosts_file | grep "\[" | tr -d "[]" | sort)
for i in $sections; do
    sed -n -e "/\[$i\]/,/\[/p" $hosts_file | sed '${/\[.*/d}'
done
