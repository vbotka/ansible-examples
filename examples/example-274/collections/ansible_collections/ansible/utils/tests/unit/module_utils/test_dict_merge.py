# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible_collections.ansible.utils.plugins.module_utils.common.utils import (
    dict_merge,
)


class TestDict_merge(unittest.TestCase):
    def test_not_dict_base(self):
        base = [0]
        other = {"a": "b"}
        expected = "must be of type <dict>"
        with self.assertRaises(Exception) as exc:
            dict_merge(base, other)
        self.assertIn(expected, str(exc.exception))

    def test_not_dict_other(self):
        base = {"a": "b"}
        other = [0]
        expected = "must be of type <dict>"
        with self.assertRaises(Exception) as exc:
            dict_merge(base, other)
        self.assertIn(expected, str(exc.exception))

    def test_simple(self):
        base = {"a": "b"}
        other = {"c": "d"}
        expected = {"a": "b", "c": "d"}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_simple_other_is_string(self):
        base = {"a": "b"}
        other = {"a": "c"}
        expected = {"a": "c"}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_simple_other_is_none(self):
        base = {"a": "b"}
        other = {"a": None}
        expected = {"a": None}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_list_value_same(self):
        base = {"a": [2, 1, 0]}
        other = {"a": [0, 1, 2]}
        expected = {"a": [0, 1, 2]}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_list_value_combine(self):
        base = {"a": [2, 1, 0]}
        other = {"a": [0, 3]}
        expected = {"a": [2, 1, 0, 3]}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_list_missing_from_other(self):
        base = {"a": [2, 1, 0]}
        other = {"b": [2, 1, 0]}
        expected = {"a": [2, 1, 0], "b": [2, 1, 0]}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_list_other_none(self):
        base = {"a": [2, 1, 0]}
        other = {"a": None}
        expected = {"a": None}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    # modified dict merge from netcommon so this works
    def test_list_other_dict(self):
        base = {"a": [2, 1, 0]}
        other = {"a": {"b": "c"}}
        expected = {"a": {"b": "c"}}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    # modified dict merge from netcommon so this works
    def test_list_other_string(self):
        base = {"a": [2, 1, 0]}
        other = {"a": "xyz"}
        expected = {"a": "xyz"}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_dict_of_dict_merged(self):
        base = {"a": {"b": 0}}
        other = {"a": {"c": 1}}
        expected = {"a": {"b": 0, "c": 1}}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_dict_of_dict_replaced(self):
        base = {"a": {"b": 0}}
        other = {"a": {"b": 1}}
        expected = {"a": {"b": 1}}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_dict_of_dict_replaced_other_none(self):
        base = {"a": {"b": 0}}
        other = {"a": None}
        expected = {"a": None}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_dict_of_dict_replaced_other_string(self):
        base = {"a": {"b": 0}}
        other = {"a": "xyz"}
        expected = {"a": "xyz"}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_dict_of_dict_replaced_other_missing(self):
        base = {"a": {"b": 0}}
        other = {"c": 1}
        expected = {"a": {"b": 0}, "c": 1}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_not_list_or_dict_different(self):
        base = {"a": 0}
        other = {"a": 1}
        expected = {"a": 1}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)

    def test_not_list_or_dict_same(self):
        base = {"a": 0}
        other = {"a": 0}
        expected = {"a": 0}
        result = dict_merge(base, other)
        self.assertEqual(result, expected)
