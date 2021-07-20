# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: multicast
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.multicast import _multicast


class TestMulticast(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _multicast()
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _multicast(ip="224.0.0.1")
        self.assertEqual(result, True)

        result = _multicast(ip="ff02::1")
        self.assertEqual(result, True)

        result = _multicast(ip="127.0.0.1")
        self.assertEqual(result, False)

        result = _multicast(ip="string")
        self.assertEqual(result, False)
