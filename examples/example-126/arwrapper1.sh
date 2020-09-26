#!/bin/bash

# All rights reserved (c) 2020, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

version="1.0.0"
runner=$HOME/bin/ansible-runner
project=$PWD/$2
param=${3:-all.yml}
usage="$(basename "$0") ver $version

Usage:
  $(basename "$0") <cmd> project [param]

Where:
  cmd ....... One of the commands: run, runid, stdout, custom, clean, test
  project ... Private data directory. See ansible-runner.
  param ..... Command specific parameter. See commands.

Commands:
  run project playbook.yml ......... Run playbook.yml in project
  runid project playbook.yml ....... The same as run plus display artifact id
  stdout project id ................ Display project/id/stdout
  custom project id ................ Display custom stat from project/id/stdout
  clean project .................... Delete project/artifacts
  test project playbook.yml ........ Test playbook.yml in project

Examples:
  arwrapper run priv9 t9.yml ....... Run playbook t9.yml in priv9
  arwrapper test priv9 t9.yml ...... Test playbook t9.yml in priv9
  arwrapper clean priv9 ............ Delete pri9/artifacts
  arwrapper stdout priv9 id1 ....... Display priv9/artifacts/id1/stdout
  arwrapper custom priv9 id1........ Display custom stat from stdout\n"

case "$1" in
    test)
	echo $(date '+%Y-%m-%d %H:%M:%S') $runner run $project -p $param
	;;
    run|runid)
	echo $(date '+%Y-%m-%d %H:%M:%S') $0
	if [ -f "$HOME/.ssh/environment" ]; then
	    source $HOME/.ssh/environment
	fi
	$runner run $project -p $param
	if [ "$1" = "runid" ]; then
	    ls -t $project/artifacts | head -1
	fi
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
