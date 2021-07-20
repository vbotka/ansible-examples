# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import unittest
from ansible.playbook.task import Task
from ansible.template import Templar

from ansible_collections.ansible.utils.plugins.action.fact_diff import (
    ActionModule,
)

try:
    from unittest.mock import MagicMock  # pylint:disable=syntax-error
except ImportError:
    from mock import MagicMock


class TestUpdate_Fact(unittest.TestCase):
    def setUp(self):
        task = MagicMock(Task)
        play_context = MagicMock()
        play_context.check_mode = False
        connection = MagicMock()
        fake_loader = {}
        templar = Templar(loader=fake_loader)
        self._plugin = ActionModule(
            task=task,
            connection=connection,
            play_context=play_context,
            loader=fake_loader,
            templar=templar,
            shared_loader_obj=None,
        )
        self._plugin._task.action = "fact_diff"
        self._task_vars = {"inventory_hostname": "mockdevice"}

    def test_argspec_no_updates(self):
        """Check passing invalid argspec"""
        self._plugin._task.args = {"before": True}
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["failed"])
        self.assertIn("missing required arguments: after", result["msg"])

    def test_same(self):
        """Ensure two equal string don't create a diff"""
        before = "Lorem ipsum dolor sit amet"
        after = before
        self._plugin._task.args = {"before": before, "after": after}
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
        self.assertEqual([], result["diff_lines"])
        self.assertEqual("", result["diff_text"])

    def test_string(self):
        """Compare two strings"""
        before = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        after = "Lorem ipsum dolor sit amet, AAA consectetur adipiscing elit"
        self._plugin._task.args = {"before": before, "after": after}
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])
        self.assertIn("-" + before, result["diff_lines"])
        self.assertIn("-" + before, result["diff_text"])
        self.assertIn("+" + after, result["diff_lines"])
        self.assertIn("+" + after, result["diff_text"])

    def test_string_skip_lines(self):
        """Compare two string, with skip_lines"""
        before = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        after = "Lorem ipsum dolor sit amet, AAA consectetur adipiscing elit"
        self._plugin._task.args = {
            "before": before,
            "after": after,
            "plugin": {"vars": {"skip_lines": "^Lorem"}},
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
        self.assertEqual([], result["diff_lines"])
        self.assertEqual("", result["diff_text"])

    def test_same_list(self):
        """Compare two lists that are the same"""
        before = [0, 1, 2, 3]
        after = before
        self._plugin._task.args = {"before": before, "after": after}
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
        self.assertEqual([], result["diff_lines"])
        self.assertEqual("", result["diff_text"])

    def test_diff_list_skip_lines(self):
        """Compare two lists, with skip_lines"""
        before = [0, 1, 2]
        after = [0, 1, 2, 3]
        self._plugin._task.args = {
            "before": before,
            "after": after,
            "plugin": {"vars": {"skip_lines": "3"}},
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
        self.assertEqual([], result["diff_lines"])
        self.assertEqual("", result["diff_text"])

    def test_diff_list(self):
        """Compare two lists with differences"""
        before = [0, 1, 2, 3]
        after = [0, 1, 2, 4]
        self._plugin._task.args = {"before": before, "after": after}
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])
        self.assertIn("-3", result["diff_lines"])
        self.assertIn("-3", result["diff_text"])
        self.assertIn("+4", result["diff_lines"])
        self.assertIn("+4", result["diff_text"])

    def test_same_dict(self):
        """Compare two dicts that are the same"""
        before = {"a": {"b": {"c": {"d": [0, 1, 2]}}}}
        after = before
        self._plugin._task.args = {"before": before, "after": after}
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
        self.assertEqual([], result["diff_lines"])
        self.assertEqual("", result["diff_text"])

    def test_diff_dict_skip_lines(self):
        """Compare two dicts, with skip_lines"""
        before = {"a": {"b": {"c": {"d": [0, 1, 2]}}}}
        after = {"a": {"b": {"c": {"d": [0, 1, 2, 3]}}}}
        self._plugin._task.args = {
            "before": before,
            "after": after,
            "plugin": {"vars": {"skip_lines": "3"}},
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
        self.assertEqual([], result["diff_lines"])
        self.assertEqual("", result["diff_text"])

    def test_diff_dict(self):
        """Compare two dicts that are different"""
        before = {"a": {"b": {"c": {"d": [0, 1, 2, 3]}}}}
        after = {"a": {"b": {"c": {"d": [0, 1, 2, 4]}}}}
        self._plugin._task.args = {"before": before, "after": after}
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])
        mlines = [
            line for line in result["diff_lines"] if re.match(r"^-\s+3$", line)
        ]
        self.assertEqual(1, len(mlines))
        mlines = [
            line
            for line in result["diff_lines"]
            if re.match(r"^\+\s+4$", line)
        ]
        self.assertEqual(1, len(mlines))

    def test_invalid_diff_engine_not_collection(self):
        """Check passing invalid argspec"""
        self._plugin._task.args = {
            "before": True,
            "after": True,
            "plugin": {"name": "a"},
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["failed"])
        self.assertIn(
            "Plugin name should be provided as a full name including collection",
            result["msg"],
        )

    def test_invalid_diff_engine_not_valid(self):
        """Check passing invalid argspec"""
        self._plugin._task.args = {
            "before": True,
            "after": True,
            "plugin": {"name": "a.b.c"},
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["failed"])
        self.assertIn("Error loading plugin 'a.b.c'", result["msg"])

    def test_invalid_regex(self):
        """Check with invalid regex"""
        before = True
        after = False
        self._plugin._task.args = {
            "before": before,
            "after": after,
            "plugin": {"vars": {"skip_lines": "+"}},
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["failed"])
        self.assertIn("The regex '+', is not valid", result["msg"])

    def test_fail_plugin(self):
        """Simulate a diff plugin failure"""
        self._plugin._result = {}
        result = self._plugin._run_diff(None)
        self.assertIsNone(result)
        self.assertTrue(self._plugin._result["failed"])
        self.assertIn(
            "'NoneType' object has no attribute 'diff'",
            self._plugin._result["msg"],
        )
