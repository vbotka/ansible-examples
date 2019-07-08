#!/bin/sh

inventory="
{
    "test": {
        "hosts": ["test_01", "test_02", "test_03"],
        "vars": {
            "ansible_connection": ssh,
            "ansible_user": admin,
            "ansible_python_interpreter": /usr/local/bin/python3.6
        }
    }
}
"


case $1 in
    --list)
	printf "$inventory"
	;;
    # --host)
    # 	printf "NOT IMPLEMENTED"
    #	exit 1
    #	;;
    *)
	exit 1
	;;
esac

exit 0
