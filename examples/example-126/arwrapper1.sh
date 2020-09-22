#!/bin/bash

# All rights reserved (c) 2020, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

version="1.0.0"

# Usage

usage="$(basename "$0") ver $version

Usage:
  $(basename "$0")  <cmd> project [param]

Where:
  cmd ....... One of the commands: run, stdout, custom, clean, test

Examples:
  arwrapper run priv9 t9.yml ....... Run playbook t9.yml in priv9
  arwrapper test priv9 t9.yml ...... Test playbook t9.yml in priv9
  arwrapper clean priv9 ............ Delete pri9/artifacts
  arwrapper stdout priv9 id ........ Display priv9/id/stdout
  arwrapper custom priv9 id ........ Display custom stat from priv9/id/stdout\n"

runner=$HOME/bin/ansible-runner
project=$PWD/$2
param=${3:-all.yml}

case "$1" in
    test)
	echo $(date '+%Y-%m-%d %H:%M:%S') $runner run $project -p $param
	;;
    run)
	echo $(date '+%Y-%m-%d %H:%M:%S') $0
	if [ -f "$HOME/.ssh/environment" ]; then
	    source $HOME/.ssh/environment
	fi
	$runner run $project -p $param
	;;
    stdout)
	cat $project/artifacts/$param/stdout
	;;
    custom)
	cat $project/artifacts/$param/stdout | \
        sed -n '/PLAY RECAP/,$p' | \
        sed -n '/CUSTOM STATS/,$p' | \
        tail -n +2 | \
	cut -d ":" -f2-
	;;
    clean)
	rm -rf $project/artifacts
	;;
    *)
	printf "$usage\n"
	exit 1
	;;
esac
exit
