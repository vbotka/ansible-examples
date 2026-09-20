# ansible_limit
https://forum.ansible.com/t/new-attribute-to-supress-the-task-trace-before-a-failing-task/46328/2

# > ansible-inventory -i hosts -l www_01,www_02 --graph
# @all:
#   |--@ungrouped:
#   |  |--localhost
#   |--@www:
#   |  |--www_01
#   |  |--www_02
#   |  |--www_03

# (penv) > ansible-playbook -i hosts -l www_01,www_02 pb.yml 
# 
# PLAY [all] **********************************************************************************
# 
# TASK [set_fact] *****************************************************************************
# ok: [www_01]
# ok: [www_02]
# 
# TASK [debug] ********************************************************************************
# ok: [www_01 -> localhost] => 
#     msg: |-
#         www_01: Running on www_01 ...
#         www_02: Running on www_02 ...
# 
# PLAY RECAP **********************************************************************************
# www_01: ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
# www_02: ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
