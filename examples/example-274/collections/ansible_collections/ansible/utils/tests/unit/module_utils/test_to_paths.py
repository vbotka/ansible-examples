# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import heapq
import os
import unittest
from ansible_collections.ansible.utils.plugins.module_utils.common.get_path import (
    get_path,
)
from ansible_collections.ansible.utils.plugins.module_utils.common.to_paths import (
    to_paths,
)

from ansible.template import Templar


class TestToPaths(unittest.TestCase):
    def setUp(self):
        self._environment = Templar(loader=None).environment

    def test_to_paths(self):
        var = {"a": {"b": {"c": {"d": [0, 1]}}}}
        expected = {"a.b.c.d[0]": 0, "a.b.c.d[1]": 1}
        result = to_paths(var, prepend=None, wantlist=None)
        self.assertEqual(result, expected)

    def test_to_paths_wantlist(self):
        var = {"a": {"b": {"c": {"d": [0, 1]}}}}
        expected = [{"a.b.c.d[0]": 0, "a.b.c.d[1]": 1}]
        result = to_paths(var, prepend=None, wantlist=True)
        self.assertEqual(result, expected)

    def test_to_paths_special_char(self):
        var = {"a": {"b": {"c": {"Eth1/1": True}}}}
        expected = [{"a.b.c['Eth1/1']": True}]
        result = to_paths(var, prepend=None, wantlist=True)
        self.assertEqual(result, expected)

    def test_to_paths_prepend(self):
        var = {"a": {"b": {"c": {"d": [0, 1]}}}}
        expected = [{"var.a.b.c.d[0]": 0, "var.a.b.c.d[1]": 1}]
        result = to_paths(var, wantlist=True, prepend="var")
        self.assertEqual(result, expected)

    def test_roundtrip_large(self):
        """Test the 1000 longest keys, otherwise this takes a _really_ long time"""
        big_json_path = os.path.join(
            os.path.dirname(__file__), "fixtures", "large.json"
        )
        with open(big_json_path) as fhand:
            big_json = fhand.read()
        var = json.loads(big_json)
        paths = to_paths(var, prepend=None, wantlist=None)
        to_tests = heapq.nlargest(1000, list(paths.keys()), key=len)
        for to_test in to_tests:
            gotten = get_path(
                var, to_test, environment=self._environment, wantlist=False
            )
            self.assertEqual(gotten, paths[to_test])

    def test_to_paths_empty_list(self):
        var = {"a": []}
        expected = {"a": []}
        result = to_paths(var, prepend=None, wantlist=None)
        self.assertEqual(result, expected)

    def test_to_paths_list_of_empty_list(self):
        var = {"a": [[], []]}
        expected = {"a[0]": [], "a[1]": []}
        result = to_paths(var, prepend=None, wantlist=None)
        self.assertEqual(result, expected)

    def test_to_paths_empty_mapping(self):
        var = {"a": {}}
        expected = {"a": {}}
        result = to_paths(var, prepend=None, wantlist=None)
        self.assertEqual(result, expected)

    def test_to_paths_list_of_empty_mapping(self):
        var = [{}, {}]
        expected = {"[0]": {}, "[1]": {}}
        result = to_paths(var, prepend=None, wantlist=None)
        self.assertEqual(result, expected)

    def test_to_paths_only_empty_list(self):
        var = []
        expected = []
        result = to_paths(var, prepend=None, wantlist=None)
        self.assertEqual(result, expected)

    def test_to_paths_only_empty_mapping(self):
        var = {}
        expected = {}
        result = to_paths(var, prepend=None, wantlist=None)
        self.assertEqual(result, expected)
