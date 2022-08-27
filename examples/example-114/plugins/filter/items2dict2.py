# -*- coding: utf-8 -*-
# Copyright (c) 2020-2022, Vladimir Botka <vbotka@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common._collections_compat import Sequence


def items2dict2(mylist, key_name='key', value_name='value', default_value=None):
    '''Takes a list of dicts with each having a 'key' and 'value' keys,
    and transforms the list into a dictionary, effectively as the
    reverse of dict2items. If 'value_name' does not exist use
    'default_value'.

    - name: Example 1
      debug:
        msg: "{{ fruits|items2dict2 }}"
      vars:
        fruits:
          - key: apple
            value: green
          - key: banana
          - key: orange

      msg:
        apple: green
        banana: null
        orange: null

    - name: Example 2
      debug:
        msg: "{{ fruits|items2dict2(key_name='k',
                                    value_name='v',
                                    default_value='undefined') }}"
      vars:
        fruits:
          - k: apple
            v: green
          - k: banana
          - k: orange

       gives:

       msg:
         apple: green
         banana: undefined
         orange: undefined
    '''

    if not isinstance(mylist, Sequence):
        raise AnsibleFilterError("First argument for community.general.items2dict2 requires a list. %s is %s" %
                                 (mylist, type(mylist)))

    return dict((item[key_name], item.setdefault(value_name, default_value)) for item in mylist)


class FilterModule(object):
    ''' Ansible filters '''

    def filters(self):
        return {
            'items2dict2': items2dict2,
        }
