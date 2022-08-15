# meta: flush_handlers

## Playbooks

- pb1.yml [OK]  Simple tasks
- pb2.yml [OK]  Simple tasks imported
- pb3.yml [OK]  Simple tasks imported and conditions
- pb4.yml [ERR] Simple tasks imported, conditions, and tags
- pb5.yml [ERR] Simple tasks tags

## Issue solved

- pb6.yml [SOLVED] Add 'tag: always' to meta

```
    - meta: flush_handlers
      tags: always
```

## Details

```
<vbotka> meta: flush_handlers does not work with tags
<vbotka> https://gist.github.com/vbotka/12c1175335b146a4d5ea43f8edbd051d
<bcoca>  most meta ignored tags (iirc we recently changed taht)
<vbotka> Am I missing something?
<bcoca>  Skipping C(meta) tasks with tags is not supported before Ansible 2.11.
<vbotka> bcoca, I dont expect meta to be skipped by tags. I expect meta to ignore the tags.
<bcoca>  since 2.11 it does not
<bcoca>  add 'always' tag if you want that
<bcoca>  implicit meta tasks (those created by the engine dymanically) automatically get always tag
<vbotka> bcoca, cool! good to know. Thank you! The 'always' tag at meta solved the problem.
```
