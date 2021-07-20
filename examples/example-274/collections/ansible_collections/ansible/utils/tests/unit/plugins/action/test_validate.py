# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.errors import AnsibleActionFail

from ansible_collections.ansible.utils.plugins.action.validate import (
    ActionModule,
)

try:
    from unittest.mock import MagicMock  # pylint:disable=syntax-error
except ImportError:
    from mock import MagicMock


DATA = {
    "GigabitEthernet0/0/0/0": {
        "auto_negotiate": False,
        "counters": {
            "in_crc_errors": 0,
            "in_errors": 0,
            "rate": {"in_rate": 0, "out_rate": 0},
        },
        "description": "configured using Ansible",
        "duplex_mode": "full",
        "enabled": True,
        "line_protocol": "up",
        "mtu": 1514,
        "oper_status": "down",
        "type": "GigabitEthernet",
    },
    "GigabitEthernet0/0/0/1": {
        "auto_negotiate": False,
        "counters": {
            "in_crc_errors": 10,
            "in_errors": 0,
            "rate": {"in_rate": 0, "out_rate": 0},
        },
        "description": "# interface is configures with Ansible",
        "duplex_mode": "full",
        "enabled": False,
        "line_protocol": "up",
        "mtu": 1514,
        "oper_status": "up",
        "type": "GigabitEthernet",
    },
}

CRITERIA_CRC_ERROR_CHECK = {
    "type": "object",
    "patternProperties": {
        "^.*": {
            "type": "object",
            "properties": {
                "counters": {
                    "properties": {
                        "in_crc_errors": {"type": "number", "maximum": 0}
                    }
                }
            },
        }
    },
}

CRITERIA_ENABLED_CHECK = {
    "type": "object",
    "patternProperties": {
        "^.*": {"type": "object", "properties": {"enabled": {"enum": [True]}}}
    },
}

CRITERIA_OPER_STATUS_UP_CHECK = {
    "type": "object",
    "patternProperties": {
        "^.*": {
            "type": "object",
            "properties": {"oper_status": {"type": "string", "pattern": "up"}},
        }
    },
}

CRITERIA_IN_RATE_CHECK = {
    "type": "object",
    "patternProperties": {
        "^.*": {
            "type": "object",
            "properties": {
                "counters": {
                    "properties": {
                        "rate": {
                            "properties": {
                                "in_rate": {"type": "number", "maximum": 0}
                            }
                        }
                    }
                }
            },
        }
    },
}


class TestValidate(unittest.TestCase):
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
        self._plugin._task.action = "validate"

    def test_invalid_argspec(self):
        """Check passing invalid argspec"""

        # missing required arguments
        self._plugin._task.args = {"engine": "ansible.utils.jsonschema"}
        result = self._plugin.run(task_vars=None)
        msg = "missing required arguments criteria data"
        for word in msg.split():
            self.assertIn(word, result["errors"])

        # invalid engine option value
        self._plugin._task.args = {
            "engine": "ansible.utils.sample",
            "data": DATA,
            "criteria": CRITERIA_OPER_STATUS_UP_CHECK,
        }
        result = self._plugin.run(task_vars=None)
        self.assertIn(
            "For engine 'ansible.utils.sample' error loading the corresponding validate plugin",
            result["msg"],
        )

        # invalid data option value
        self._plugin._task.args = {
            "engine": "ansible.utils.jsonschema",
            "data": "invalid data",
            "criteria": CRITERIA_OPER_STATUS_UP_CHECK,
        }

        with self.assertRaises(AnsibleActionFail) as error:
            self._plugin.run(task_vars=None)
        self.assertIn("'data' option value is invalid", str(error.exception))

        # invalid criteria option value
        self._plugin._task.args = {
            "engine": "ansible.utils.jsonschema",
            "data": DATA,
            "criteria": "invalid criteria",
        }

        with self.assertRaises(AnsibleActionFail) as error:
            self._plugin.run(task_vars=None)
        self.assertIn(
            "'criteria' option value is invalid", str(error.exception)
        )

    def test_invalid_validate_plugin_config_options(self):
        """Check passing invalid validate plugin options"""

        self._plugin._task.args = {
            "engine": "ansible.utils.jsonschema",
            "data": DATA,
            "criteria": CRITERIA_IN_RATE_CHECK,
        }

        result = self._plugin.run(
            task_vars={"ansible_validate_jsonschema_draft": "draft0"}
        )
        self.assertIn(
            "value of draft must be one of: draft3, draft4, draft6, draft7, got: draft0",
            result["msg"],
        )

    def test_invalid_data(self):
        """Check passing invalid data as per criteria"""

        self._plugin._task.args = {
            "engine": "ansible.utils.jsonschema",
            "data": DATA,
            "criteria": [
                CRITERIA_CRC_ERROR_CHECK,
                CRITERIA_ENABLED_CHECK,
                CRITERIA_OPER_STATUS_UP_CHECK,
            ],
        }

        result = self._plugin.run(task_vars=None)
        self.assertIn(
            "patternProperties.^.*.properties.counters.properties.in_crc_errors.maximum",
            result["msg"],
        )
        self.assertIn(
            "patternProperties.^.*.properties.enabled.enum", result["msg"]
        )
        self.assertIn(
            "'patternProperties.^.*.properties.oper_status.pattern",
            result["msg"],
        )

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        self._plugin._task.args = {
            "engine": "ansible.utils.jsonschema",
            "data": DATA,
            "criteria": CRITERIA_IN_RATE_CHECK,
        }

        result = self._plugin.run(task_vars=None)
        self.assertIn("all checks passed", result["msg"])
