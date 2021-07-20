# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.module_utils.common.utils import (
    sort_list,
)


class TestSortList(unittest.TestCase):
    def test_simple(self):
        var = [3, 2, 1]
        result = sort_list(var)
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_mot_list(self):
        var = {"a": "b"}
        result = sort_list(var)
        self.assertEqual(result, var)

    def test_not_same(self):
        var = [{"a": "b", "c": "d"}, {"b": "a"}]
        expected = "dictionaries do not match"
        with self.assertRaises(Exception) as exc:
            sort_list(var)
        self.assertIn(expected, str(exc.exception))

    def test_pass(self):
        var = [{"a": 2, "b": 3}, {"a": 0, "b": 1}]
        expected = [{"a": 0, "b": 1}, {"a": 2, "b": 3}]
        result = sort_list(var)
        self.assertEqual(result, expected)
