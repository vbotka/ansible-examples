#!/usr/bin/python

# 'Best way to modify json in ansible' Copyright 2017, stackoverflow.com
# https://stackoverflow.com/questions/46025695/best-way-to-modify-json-in-ansible
# CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/legalcode
# Copyright 2021, Vladimir Botka <vbotka@gmail.com>
# GNU General Public License v3.0+ https://www.gnu.org/licenses/gpl-3.0.txt
# (https://www.gnu.org/licenses/license-compatibility.en.html)

from __future__ import absolute_import, division, print_function                              
__metaclass__ = type                                                                          

                                                                                     
DOCUMENTATION = r'''
---
module: json_modify
short_description: Modify JSON data
description:
  - This module modifies JSON data
options:
  data:
    description:
      - JSON data
    required: true
    type: dict
  pointer:
    description:
      - JSON pointer
    required: true
    type: path
  action:
    description:
      - Action to take. C(append) to pointer, C(extend) the list, and C(update) the dictionary
    required: true
    type: string
    choices: [ "append", "extend", "update" ]
  update:
    description:
      - Update pointer
    type: dict
  extend:
    description:
      - Extend pointer
    type: list
  append:
    description:
      - Append to pointer
author:
    - "(@vbotka)"
requirements:
    - python-json-pointer
'''

# TODO: EXAMPLES, RETURN

import json
from ansible.module_utils.basic import AnsibleModule, missing_required_lib                    


try:
    import jsonpointer
except ImportError:
    jsonpointer = None


def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(required=True, type='dict'),
            pointer=dict(required=True, type='path'),
            action=dict(required=True, type='str',
                        choices=['append', 'extend', 'update']),
            update=dict(type='dict'),
            extend=dict(type='list'),
            append=dict(),
        ),
        supports_check_mode=True,
    )

    if jsonpointer is None:
        module.fail_json(msg='jsonpointer module is not available')

    action = module.params['action']
    data = module.params['data']
    pointer = module.params['pointer']

    if isinstance(data, str):
        data = json.loads(str)

    try:
        res = jsonpointer.resolve_pointer(data, pointer)
    except jsonpointer.JsonPointerException as err:
        module.fail_json(msg=str(err))

    if action == 'append':
        res.append(module.params['append'])
    if action == 'extend':
        res.extend(module.params['extend'])
    elif action == 'update':
        res.update(module.params['update'])

    module.exit_json(changed=True,
                     result=data)


if __name__ == '__main__':
    main()
