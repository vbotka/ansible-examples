# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.module_utils.common.get_path import (
    get_path,
)


from ansible.template import Templar


class TestGetPath(unittest.TestCase):
    def setUp(self):
        self._environment = Templar(loader=None).environment

    def test_get_path_pass(self):
        var = {"a": {"b": {"c": {"d": [0, 1]}}}}
        path = "a.b.c.d[0]"
        result = get_path(
            var, path, environment=self._environment, wantlist=False
        )
        expected = "0"
        self.assertEqual(result, expected)

    def test_get_path_pass_wantlist(self):
        var = {"a": {"b": {"c": {"d": [0, 1]}}}}
        path = "a.b.c.d[0]"
        result = get_path(
            var, path, environment=self._environment, wantlist=True
        )
        expected = ["0"]
        self.assertEqual(result, expected)

    def test_get_path_fail(self):
        var = {"a": {"b": {"c": {"d": [0, 1]}}}}
        path = "a.b.e"
        expected = "dict object' has no attribute 'e'"
        with self.assertRaises(Exception) as exc:
            get_path(var, path, environment=self._environment, wantlist=False)
        self.assertIn(expected, str(exc.exception))
