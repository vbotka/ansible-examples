# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: ipv4_hostmask
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.ipv4_hostmask import (
    _ipv4_hostmask,
)


class TestIpV4Hostmask(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _ipv4_hostmask()
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _ipv4_hostmask(ip="0.1.255.255")
        self.assertEqual(result, True)

        result = _ipv4_hostmask(ip="255.255.255.0")
        self.assertEqual(result, False)

        result = _ipv4_hostmask(ip="10.1.1.1")
        self.assertEqual(result, False)

        result = _ipv4_hostmask(ip="string")
        self.assertEqual(result, False)
