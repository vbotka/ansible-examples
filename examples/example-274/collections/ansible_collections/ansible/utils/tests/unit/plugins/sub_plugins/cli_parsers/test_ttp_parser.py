# (c) 2020 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

import pytest

from ansible_collections.ansible.utils.tests.unit.compat import unittest
from ansible_collections.ansible.utils.plugins.sub_plugins.cli_parser.ttp_parser import (
    CliParser,
)

textfsm = pytest.importorskip("ttp")


class TestTextfsmParser(unittest.TestCase):
    def test_ttp_parser(self):
        nxos_cfg_path = os.path.join(
            os.path.dirname(__file__), "fixtures", "nxos_show_version.cfg"
        )
        nxos_template_path = os.path.join(
            os.path.dirname(__file__), "fixtures", "nxos_show_version.ttp"
        )

        with open(nxos_cfg_path) as fhand:
            nxos_show_version_output = fhand.read()

        task_args = {
            "text": nxos_show_version_output,
            "parser": {
                "name": "ansible.utils.ttp",
                "command": "show version",
                "template_path": nxos_template_path,
            },
        }
        parser = CliParser(task_args=task_args, task_vars=[], debug=False)

        result = parser.parse()
        # import pdb; pdb.set_trace()
        parsed_output = [
            {
                "boot_image": "bootflash:///nxos.7.0.3.I7.1.bin",
                "os": "7.0(3)I7(1)",
                "platform": "9000v",
                "uptime": "12 day(s), 23 hour(s), 48 minute(s), 10 second(s)",
            }
        ]
        self.assertEqual(result["parsed"][0][0], parsed_output)

    def test_textfsm_parser_invalid_parser(self):
        fake_path = "/ /I hope this doesn't exist"
        task_args = {
            "text": "",
            "parser": {
                "name": "ansible.utils.ttp",
                "command": "show version",
                "template_path": fake_path,
            },
        }
        parser = CliParser(task_args=task_args, task_vars=[], debug=False)
        result = parser.parse()
        errors = {
            "errors": "error while reading template_path file {0}".format(
                fake_path
            )
        }
        self.assertEqual(result, errors)
