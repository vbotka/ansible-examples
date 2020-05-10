#!/bin/bash

lf="my_list.log"
la="my_list.log.all"
ef="my_list.err"
ea="my_list.err.all"
pd="private5/project"
tf="test_file"
ad="private5/artifacts/ID01"

cat /dev/null > $la
cat /dev/null > $ea
cat /dev/null > $pd/$tf
rm -rf $ad

export ANSIBLE_STDOUT_CALLBACK=null
for i in {1..10}; do
    ansible-runner -p test3.yml -i ID01 run private5 > /dev/null && echo [ok ] [$i] ansible-runner
    ansible-playbook play5.yml && echo [ok ] [$i] ansible-playbook
    lines_test=`cat $pd/$tf | wc -l`
    lines_log=`cat $lf | wc -l`
    [ "$lines_test" -ne "$lines_log" ] && echo "[err] [$i] written: $lines_test log: $lines_log"
    (cd $pd;  mv $tf $i-$tf)
    cat /dev/null > $lf
    rm -rf $ad
done

[ -s $ea ] && echo "[err] See list of errors in $ea"
exit 0
