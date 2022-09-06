# All rights reserved (c) 2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import string_types
from mac_vendor_lookup import MacLookup


def mac_vendor_lookup(mac):
    if not isinstance(mac, string_types):
        raise AnsibleFilterError('The argument for mac_lookup must be string. %s is %s' %
                                 (mac, type(mac)))
    try:
        vendor = MacLookup().lookup(mac)
    except KeyError:
        vendor = 'Prefix is not registered'

    return vendor


class FilterModule(object):
    ''' Ansible wrapper for Mac Vendor Lookup '''

    def filters(self):
        return {
            'mac_vendor_lookup': mac_vendor_lookup,
        }
