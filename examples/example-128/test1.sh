#!/bin/sh
cd /scratch
servername=`hostname -f`
echo ${servername} >> ansible.log
echo "begin of the section" >> ansible.log
 
