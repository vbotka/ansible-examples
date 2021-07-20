# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: subnet_of
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.subnet_of import _subnet_of


class TestSubnetOf(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _subnet_of()
        self.assertIn("argument", str(error.exception))

        with self.assertRaises(TypeError) as error:
            _subnet_of(network_a="10.1.1.0/24")
        self.assertIn("argument", str(error.exception))

        with self.assertRaises(TypeError) as error:
            _subnet_of(network_b="10.0.0.0/8")
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _subnet_of(network_a="10.1.1.0/24", network_b="10.0.0.0/8")
        self.assertEqual(result, True)

        result = _subnet_of(network_a="10.0.0.0/8", network_b="10.1.1.0/24")
        self.assertEqual(result, False)

        result = _subnet_of(network_a="192.168.1.0/24", network_b="10.0.0.0/8")
        self.assertEqual(result, False)
