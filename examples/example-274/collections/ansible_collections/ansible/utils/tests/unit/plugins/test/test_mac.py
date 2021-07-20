# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: mac
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.mac import _mac


class TestMac(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _mac()
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _mac(mac="02:16:3e:e4:16:f3")
        self.assertEqual(result, True)

        result = _mac(mac="02-16-3e-e4-16-f3")
        self.assertEqual(result, True)

        result = _mac(mac="0216.3ee4.16f3")
        self.assertEqual(result, True)

        result = _mac(mac="02163ee416f3")
        self.assertEqual(result, True)

        result = _mac(mac="string")
        self.assertEqual(result, False)
