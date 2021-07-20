# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: ipv4_address
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.ipv4_address import (
    _ipv4_address,
)


class TestIpV4Address(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _ipv4_address()
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _ipv4_address(ip="10.1.1.1")
        self.assertEqual(result, True)

        result = _ipv4_address(ip="10.0.0.0/8")
        self.assertEqual(result, False)

        result = _ipv4_address(ip="2001:db8:a::123")
        self.assertEqual(result, False)

        result = _ipv4_address(ip="string")
        self.assertEqual(result, False)
