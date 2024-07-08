# -*- coding: utf-8 -*-
# Copyright (c) 2024 Vladimir Botka <vbotka@gmail.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common._collections_compat import Mapping

DOCUMENTATION = '''
    name: reveal_ansible_type
    short_description: Return input type
    version_added: "9.2.0"
    author: Vladimir Botka (@vbotka)
    description: This filter returns input type.
    options:
      _input:
        description: Input data.
        type: any
        required: true
      alias:
        description: Type aliases.
        default: {}
        type: dictionary
'''

EXAMPLES = '''
    - debug:
        msg: "{{ data | reveal_ansible_type }}"
      vars:
        data: [{a: 1}, {b: 2}]

    # gives

      msg: list[dict]
'''

RETURN = '''
  _value:
    description: Type of the input.
    type: str
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


def my_reveal_ansible_type(data, alias={}):
    """return data type"""

    if not isinstance(alias, Mapping):
        msg = "Argument alias must be a dictionary. %s is %s"
        raise AnsibleFilterError(msg % (alias, type(alias)))

    return _ansible_type(data, alias)


class FilterModule(object):

    def filters(self):
        return {
            'my_reveal_ansible_type': my_reveal_ansible_type
        }
