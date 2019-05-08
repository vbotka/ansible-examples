#!/bin/bash
sections=$(cat hosts | grep "\[")
# echo $sections
set -- $sections
while [ ! -z "$2" ]
do
    echo "$1 $2"
    echo "-----------------------------------------------"
# TODO: print groups
#    
#   sed -e '/'"$1"'/'"$2"'/p' hosts
#   sed -n "/webservers/,/database/p" hosts
#   awk '/\[webservers\]/,/\[database\]/' hosts
#   awk '/([webservers])/,/([database])/' hosts
#   awk '/'"$1"'/,/'"$2"'/' hosts
    echo "-----------------------------------------------"
    shift 
done
