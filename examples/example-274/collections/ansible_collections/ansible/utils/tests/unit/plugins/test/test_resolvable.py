# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for netaddr test plugin: resolvable
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.test.resolvable import (
    _resolvable,
)


class TestResolvable(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # missing argument
        with self.assertRaises(TypeError) as error:
            _resolvable()
        self.assertIn("argument", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        result = _resolvable(host="www.google.com")
        self.assertEqual(result, True)

        result = _resolvable(host="127.0.0.1")
        self.assertEqual(result, True)

        result = _resolvable(host="::1")
        self.assertEqual(result, True)

        result = _resolvable(host="foo.google.com")
        self.assertEqual(result, False)

        result = _resolvable(host="invalidhost")
        self.assertEqual(result, False)
