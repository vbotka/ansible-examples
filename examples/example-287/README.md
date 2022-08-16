# Job management

Run script asynchronously and use signals.


## Example 1. Configure the controller


### Inventory

```
shell> cat hosts
[test]
test_11
test_12
test_13
```


### Don't display skipped and ok hosts

```
shell> export ANSIBLE_DISPLAY_OK_HOSTS=false
shell> export ANSIBLE_DISPLAY_SKIPPED_HOSTS=false
```


### Configure logger at the controller

Set *logger.enable=true* and fit other attributes of the dictionary
*logger* to your needs

```yaml
shell> ansible-playbook pb.yml -e create_logger=true -t create_logger

PLAY [all] *******************************************************************************

PLAY RECAP *******************************************************************************
test_11: ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
test_12: ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
test_13: ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

The configuration file will be created.

```
shell> cat /etc/rsyslog.d/90-ansibletest.conf
local6.*			-/var/log/ansibletest.log
```

### Copy the script to remote hosts

Use the script below for testing. By default, the script will set trap
to the signals SIGINT and SIGTERM, and write *pidifle*. Then will wait
90s, send PID to stdout, delete the *pidfile* and
terminate. Optionally, it will count in 1s steps to stdout.

```
shell> cat files/sleep90.sh
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
```

```
shell> ansible-playbook pb.yml -e copy_script=true -t copy_script

PLAY [all] *******************************************************************************

TASK [Copy script] ***********************************************************************
changed: [test_12]
changed: [test_11]
changed: [test_13]

PLAY RECAP *******************************************************************************
test_11: ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
test_12: ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
test_13: ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

### Test sanity

```
shell> ansible-playbook pb.yml -e sanity_job=true -t sanity_job

PLAY [all] *******************************************************************************

PLAY RECAP *******************************************************************************
test_11: ok=7    changed=0    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
test_12: ok=6    changed=0    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
test_13: ok=6    changed=0    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0
```

## Example 2. Run the scripts at the remote hosts and wait until module async_status finds the job finished


### Run the scripts at the remote hosts

Start job asynchronously

```
shell> ansible-playbook pb.yml -e start_job=true -t start_job

PLAY [all] *******************************************************************************

TASK [Start job concurrently] ************************************************************
changed: [test_12]
changed: [test_13]
changed: [test_11]

RUNNING HANDLER [start job logger] *******************************************************
changed: [test_12 -> localhost]
changed: [test_13 -> localhost]
changed: [test_11 -> localhost]

RUNNING HANDLER [Start job. 93.Write my_cache_all] ***************************************
changed: [test_12 -> localhost]

PLAY RECAP *******************************************************************************
test_11: ok=7    changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
test_12: ok=8    changed=3    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
test_13: ok=6    changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0
```

Take a look at the log

```
shell> tail -f /var/log/ansibletest.log 
Aug 16 07:07:54 localhost root: [test_12] started pid: 69197 [async] ansible_job_id: 213217395172.69143
Aug 16 07:07:54 localhost root: [test_13] started pid: 69195 [async] ansible_job_id: 427811916767.69144
Aug 16 07:07:54 localhost root: [test_11] started pid: 69193 [async] ansible_job_id: 356086607051.69142
```

Take a look at the cache

```
shell> cat /tmp/ansible-test.cache 
my_cache_all:
  test_11:
      sleep90.sh:
          ansible_job_id: '356086607051.69142'
          job_pid: '69193'
          running: true
  test_12:
      sleep90.sh:
          ansible_job_id: '213217395172.69143'
          job_pid: '69197'
          running: true
  test_13:
      sleep90.sh:
          ansible_job_id: '427811916767.69144'
          job_pid: '69195'
          running: true
```


### Wait until module async_status finds the job finished

```
shell> ansible-playbook pb.yml -e async_job=true -t async_job

PLAY [all] *******************************************************************************

TASK [Check on an async job] *************************************************************
changed: [test_11]
changed: [test_12]
changed: [test_13]

RUNNING HANDLER [stop job logger] ********************************************************
changed: [test_13 -> localhost]
changed: [test_12 -> localhost]
changed: [test_11 -> localhost]

RUNNING HANDLER [Stop job. 93.Write my_cache_all] ****************************************
changed: [test_11 -> localhost]

PLAY RECAP *******************************************************************************
test_11: ok=8    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
test_12: ok=5    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
test_13: ok=5    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
```

Take a look at the log

```
shell> tail -f /var/log/ansibletest.log 
Aug 16 07:07:54 localhost root: [test_12] started pid: 69197 [async] ansible_job_id: 213217395172.69143
Aug 16 07:07:54 localhost root: [test_13] started pid: 69195 [async] ansible_job_id: 427811916767.69144
Aug 16 07:07:54 localhost root: [test_11] started pid: 69193 [async] ansible_job_id: 356086607051.69142
Aug 16 07:10:41 localhost root: [test_13] stopped pid: 69195 [async] rc: 0
Aug 16 07:10:41 localhost root: [test_12] stopped pid: 69197 [async] rc: 0
Aug 16 07:10:41 localhost root: [test_11] stopped pid: 69193 [async] rc: 0
```

Take a look at the cache

```yaml
shell> cat /tmp/ansible-test.cache 
my_cache_all:
  test_11:
      sleep90.sh:
          running: false
  test_12:
      sleep90.sh:
          running: false
  test_13:
      sleep90.sh:
          running: false
```


## Example 3. Run the scripts at the remote hosts, terminate the job at host_12, and wait until module async_status finds the other jobs finished


### Run the scripts at the remote hosts

Run the scripts at the remote hosts the same ways as in Example 2.

Take a look at the log

```
shell> tail -f /var/log/ansibletest.log 
Aug 16 07:24:13 localhost root: [test_11] started pid: 70125 [async] ansible_job_id: 697365068006.70074
Aug 16 07:24:13 localhost root: [test_12] started pid: 70128 [async] ansible_job_id: 535736836948.70076
Aug 16 07:24:13 localhost root: [test_13] started pid: 70127 [async] ansible_job_id: 853669171817.70075
```


### Terminate the job at host_12

```
shell> ansible-playbook pb.yml -e stop_job=true -t stop_job -e signal=TERM --limit test_12

PLAY [all] *******************************************************************************

TASK [Stop job] **************************************************************************
changed: [test_12]

RUNNING HANDLER [stop job logger] ********************************************************
changed: [test_12 -> localhost]

RUNNING HANDLER [Stop job. 93.Write my_cache_all] ****************************************
changed: [test_12 -> localhost]

PLAY RECAP *******************************************************************************
test_12: ok=10   changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
```

Take a look at the log

```
shell> tail -f /var/log/ansibletest.log 
Aug 16 07:24:13 localhost root: [test_11] started pid: 70125 [async] ansible_job_id: 697365068006.70074
Aug 16 07:24:13 localhost root: [test_12] started pid: 70128 [async] ansible_job_id: 535736836948.70076
Aug 16 07:24:13 localhost root: [test_13] started pid: 70127 [async] ansible_job_id: 853669171817.70075
Aug 16 07:24:46 localhost root: [test_12] stopped pid: 70128 [SIGTERM] rc: 0
```

Take a look at the cache

```
shell> cat /tmp/ansible-test.cache 
my_cache_all:
  test_11:
      sleep90.sh:
          ansible_job_id: '697365068006.70074'
          job_pid: '70125'
          running: true
  test_12:
      sleep90.sh:
          running: false
  test_13:
      sleep90.sh:
          ansible_job_id: '853669171817.70075'
          job_pid: '70127'
          running: true
```

### Wait until module *async_status* finds the other job finished


```
shell> ansible-playbook pb.yml -e async_job=true -t async_job

PLAY [all] *******************************************************************************

TASK [Check on an async job] *************************************************************
changed: [test_11]
changed: [test_13]

RUNNING HANDLER [stop job logger] ********************************************************
changed: [test_13 -> localhost]
changed: [test_11 -> localhost]

RUNNING HANDLER [Stop job. 93.Write my_cache_all] ****************************************
changed: [test_11 -> localhost]

PLAY RECAP *******************************************************************************
test_11: ok=8    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
test_12: ok=1    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
test_13: ok=5    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
```

Take a look at the log

```
shell> tail -f /var/log/ansibletest.log 
Aug 16 07:24:13 localhost root: [test_11] started pid: 70125 [async] ansible_job_id: 697365068006.70074
Aug 16 07:24:13 localhost root: [test_12] started pid: 70128 [async] ansible_job_id: 535736836948.70076
Aug 16 07:24:13 localhost root: [test_13] started pid: 70127 [async] ansible_job_id: 853669171817.70075
Aug 16 07:24:46 localhost root: [test_12] stopped pid: 70128 [SIGTERM] rc: 0
Aug 16 07:29:56 localhost root: [test_13] stopped pid: 70127 [async] rc: 0
Aug 16 07:29:56 localhost root: [test_11] stopped pid: 70125 [async] rc: 0
```

Take a look at the cache

```
shell> cat /tmp/ansible-test.cache 
my_cache_all:
  test_11:
      sleep90.sh:
          running: false
  test_12:
      sleep90.sh:
          running: false
  test_13:
      sleep90.sh:
          running: false
```
