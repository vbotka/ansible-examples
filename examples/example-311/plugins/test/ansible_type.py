# -*- coding: utf-8 -*-
# Copyright (c) 2024 Vladimir Botka <vbotka@gmail.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common._collections_compat import Mapping, Sequence

DOCUMENTATION = '''
    name: ansible_type
    short_description: Validate input type
    version_added: "9.2.0"
    author: Vladimir Botka (@vbotka)
    description: This test validates input type.
    options:
      _input:
        description: Input data.
        type: raw
        required: true
      dtype:
        description: A single data type, or a data types list to be validated.
        type: raw
        required: true
      alias:
        description: Data type aliases.
        default: {}
        type: dictionary
'''

EXAMPLES = '''
    - debug:
        msg: "{{ data is ansible_type(dtype='list[dict]') }}"
      vars:
        data:
          - '[{a: 1}, {b: 2}]'

    # gives

      msg: true
'''

RETURN = '''
  _value:
    description: Whether the data type is valid.
    type: bool
'''


def _atype(data, alias):

    data_type = type(data).__name__

    if data_type in alias:
        return alias[data_type]

    return data_type


def _ansible_type(data, alias):

    data_type = _atype(data, alias)

    if data_type == 'list' and len(data) > 0:
        items = [_atype(i, alias) for i in data]
        items_type = '|'.join(sorted(set(items)))
        return ''.join((data_type, '[', items_type, ']'))

    if data_type == 'dict' and len(data) > 0:
        keys = [_atype(i, alias) for i in data.keys()]
        vals = [_atype(i, alias) for i in data.values()]
        keys_type = '|'.join(sorted(set(keys)))
        vals_type = '|'.join(sorted(set(vals)))
        return ''.join((data_type, '[', keys_type, ', ', vals_type, ']'))

    return data_type


def my_ansible_type(data, dtype, alias={}):
    """validate data type"""

    if not isinstance(alias, Mapping):
        msg = "The argument alias must be a dictionary. %s is %s"
        raise AnsibleFilterError(msg % (alias, type(alias)))

    if not isinstance(dtype, Sequence):
        msg = "The argument dtype must be a string or a list. dtype is %s."
        raise AnsibleFilterError(msg % (dtype, type(dtype)))

    if isinstance(dtype, list):
        data_types = dtype
    else:
        data_types = [dtype]

    return _ansible_type(data, alias) in data_types


class TestModule(object):

    def tests(self):
        return {
            'my_ansible_type': my_ansible_type
        }
