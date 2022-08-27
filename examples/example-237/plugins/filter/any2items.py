# -*- coding: utf-8 -*-
# Copyright (c) 2020-2022, Vladimir Botka <vbotka@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import string_types
from ansible.module_utils.common._collections_compat import Mapping, Sequence


def any2items(x, key='key', override=False):
    ''' Convert any input to list.

    Example 1:

    - name: No changes to a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits: [apple, banana, orange]

       gives:

       msg:
         - apple
         - banana
         - orang

    Example 2:

    - name: Convert string to first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits: 'apple'

       gives:

       msg:
         - apple

    Example 3:

    - name: Convert None to first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits: None

       gives:

       msg:
         - None

    Example 4:

    - name: Convert dictionary where all values are dictionaries to a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits:
          apple:
            color: green
            size: big
          banana:
            color: yellow
            size: small

       gives:

       msg:
         - color: green
           key: apple
           size: big
         - color: yellow
           key: banana
           size: small

    Example 5:

    - name: Same as the above but change key name
      debug:
        msg: "{{ fruits|any2items(key='name') }}"
      vars:
        fruits:
          apple:
            color: green
            size: big
          banana:
            color: yellow
            size: small

       gives:

       msg:
         - color: green
           name: apple
           size: big
         - color: yellow
           name: banana
           size: small

    Example 6:

    - name: Convert dictionary where NOT all values are dictionaries
            to a first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits:
          apple:
            color: green
            size: big
          banana:
            color: yellow
            size: small
          orange: ripe

       gives:

       msg:
         - apple:
             color: green
             size: big
           banana:
             color: yellow
             size: small
           orange: ripe

    Example 7:

    - name: Convert dictionary where NOT all values are dictionaries
            to a first item in a list
      debug:
        msg: "{{ fruits|any2items }}"
      vars:
        fruits:
          apple: green
          banana: yellow
          orange: ripe

       gives:

       msg:
         - apple: green
           banana: yellow
           orange: ripe

    Example 8:

    - name: Iterate any data by any2items
      debug:
        var: item
      loop: "{{ [{'a': 1},{'b': 2}]|any2items }}"

    - name: Iterate any data by any2items
      debug:
        var: item
      loop: "{{ {'c': 3}|any2items }}"

    '''

    if not isinstance(key, string_types):
        raise AnsibleFilterError('Argument key for any2items must be string. %s is %s' %
                                 (key, type(key)))
    if not isinstance(override, bool):
        raise AnsibleFilterError('Argument override for any2items must be boollean. %s is %s' %
                                 (override, type(override)))

    if isinstance(x, Mapping):
        keys = list(x.keys())
        values = list(x.values())
        if all(isinstance(value, Mapping) for value in values):
            if (not override) and any(key in list(value.keys()) for value in values):
                raise AnsibleFilterError('Key %s present in the dictionary.' % (key))
            else:
                _l = values
                for idx, item in enumerate(values):
                    _z = item.copy()
                    _z.update({key: keys[idx]})
                    _l[idx] = _z
        else:
            _l = []
            _l.insert(0, x)
        return _l
    elif isinstance(x, string_types):
        _l = []
        _l.insert(0, x)
        return _l
    elif isinstance(x, Sequence):
        _l = list(x)
        return _l
    else:
        _l = []
        _l.insert(0, x)
        return _l


class FilterModule(object):
    ''' Ansible filters '''

    def filters(self):
        return {
            'any2items': any2items,
        }
