#!/bin/sh

case $1 in

    host1)
	printf "mac address of host1"
	;;

    host2)
	printf "mac address of host2"
	;;

    *)
	printf "unknown host"
	exit 1
	;;

esac

exit 0
