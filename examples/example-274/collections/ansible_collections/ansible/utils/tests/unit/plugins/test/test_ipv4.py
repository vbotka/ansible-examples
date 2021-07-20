# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: ipv4
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.ipv4 import _ipv4


class TestIpV4(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _ipv4()
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _ipv4(ip="10.1.1.1")
        self.assertEqual(result, True)

        result = _ipv4(ip="10.0.0.0/8")
        self.assertEqual(result, True)

        result = _ipv4(ip="2001:db8:a::123")
        self.assertEqual(result, False)

        result = _ipv4(ip="string")
        self.assertEqual(result, False)
