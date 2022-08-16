#!/bin/sh

timeout=${1:-90}
counter=${2:-none}

basename=${0##*/}
pidfile=/var/run/${basename%.*}.pid
[ -f ${pidfile} ] && exit 0

trap 'rm ${pidfile}
exit 0' SIGINT SIGTERM

echo $$ > ${pidfile}

i=1
if [ ${counter} == 'counter' ]; then
    echo ${i}
fi
while [ ${i} -lt ${timeout} ]
do
    sleep 1
    i=$(($i+1))
    if [ ${counter} == 'counter' ]; then
	echo -e '\e[1A\e[K'${i}
    fi
done

cat ${pidfile}
rm ${pidfile}
exit 0
