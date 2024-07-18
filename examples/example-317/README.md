# Ansible lint

* key-order[task]

```yaml
    - name: Test tags after the block
      block:

        - name: Ddebug
          ansible.builtin.debug:
            msg: task 1
        - name: Debug
          ansible.builtin.debug:
            msg: task 2

      tags: t1
```

```yaml
(env) > ansible-lint pb1.yml

  ...

key-order[task]: You can improve the task key order to: name, tags, block
pb1.yml:6 Task/Handler: Test tags after the block

Read documentation for instructions on how to ignore specific rule violations.

               Rule Violation Summary               
 count tag             profile rule associated tags 
     1 key-order[task] basic   formatting           

Failed: 1 failure(s), 0 warning(s) on 1 files. Last profile that met the validation criteria was 'min'.
```
