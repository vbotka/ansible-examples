ansible-runner
==============
https://ansible-runner-role.readthedocs.io


How do i count task success/failure in ansible?
-----------------------------------------------
See play3.yml Example:

```yaml
     "item": {
         "counter": 12,
         "event": "runner_on_failed",
         "host": "test_02",
         "task": "fail"
     }
```


Test role vbotka.ansible_lib tasks_from: al_runner_events
---------------------------------------------------------
See play4.yml, play5.yml


Bug: set ANSIBLE_CALLBACK_PLUGINS in envvars is not working. #219
-----------------------------------------------------------------
https://github.com/ansible/ansible-runner/issues/219

See play6.yml
The callback is always awx_display.
