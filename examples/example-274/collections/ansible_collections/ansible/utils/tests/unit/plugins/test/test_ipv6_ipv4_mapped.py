# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: ipv6_ipv4_mapped
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.ipv6_ipv4_mapped import (
    _ipv6_ipv4_mapped,
)


class TestIpV6IpV4Mapped(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _ipv6_ipv4_mapped()
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _ipv6_ipv4_mapped(ip="::FFFF:10.1.1.1")
        self.assertEqual(result, True)

        result = _ipv6_ipv4_mapped(ip="::AAAA:10.1.1.1")
        self.assertEqual(result, False)

        result = _ipv6_ipv4_mapped(ip="string")
        self.assertEqual(result, False)
