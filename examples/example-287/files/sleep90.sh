#!/bin/sh

PIDFILE=/var/run/sleep90.pid
[ -f $PIDFILE ] && exit 0

trap 'rm ${PIDFILE}
exit 0' SIGINT SIGTERM

echo $$ > ${PIDFILE}

i=1
while [ $i -lt 90 ]
do
    sleep 1
    i=$(($i+1))
done

cat ${PIDFILE}
rm ${PIDFILE}
exit 0
