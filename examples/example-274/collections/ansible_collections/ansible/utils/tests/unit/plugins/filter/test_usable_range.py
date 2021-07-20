# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit test file for usable_range filter plugin
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from ansible.errors import AnsibleError
from ansible_collections.ansible.utils.plugins.filter.usable_range import (
    _usable_range,
)

INVALID_DATA_1 = [
    "helloworld",
    "192.0.2.0/23/24",
    "::/20/30",
    "10.0.0.0/322",
    "2001:db8:abcd:0012::0/129",
]
INVALID_DATA_2 = ["192.168.1.25/24", "2001:db8:abcd:12::2/126"]

VALID_DATA = [
    "10.0.0.8/30",
    "192.0.2.0/28",
    "2001:db8:abcd:0012::0/126",
    "2001:DB8:ABCD:12::",
]

VALID_OUTPUT_1 = {
    "number_of_ips": 4,
    "usable_ips": ["10.0.0.8", "10.0.0.9", "10.0.0.10", "10.0.0.11"],
}
VALID_OUTPUT_2 = {
    "number_of_ips": 16,
    "usable_ips": [
        "192.0.2.0",
        "192.0.2.1",
        "192.0.2.2",
        "192.0.2.3",
        "192.0.2.4",
        "192.0.2.5",
        "192.0.2.6",
        "192.0.2.7",
        "192.0.2.8",
        "192.0.2.9",
        "192.0.2.10",
        "192.0.2.11",
        "192.0.2.12",
        "192.0.2.13",
        "192.0.2.14",
        "192.0.2.15",
    ],
}

VALID_OUTPUT_3 = {
    "number_of_ips": 4,
    "usable_ips": [
        "2001:db8:abcd:12::",
        "2001:db8:abcd:12::1",
        "2001:db8:abcd:12::2",
        "2001:db8:abcd:12::3",
    ],
}
VALID_OUTPUT_4 = {"number_of_ips": 1, "usable_ips": ["2001:db8:abcd:12::"]}


class TestUsableRange(unittest.TestCase):
    def setUp(self):
        pass

    def test_missing_data(self):
        """Check passing missing argspec"""

        # missing required arguments
        ip = ""
        with self.assertRaises(AnsibleError) as error:
            _usable_range(ip)
        self.assertIn(
            "does not appear to be an IPv4 or IPv6 network",
            str(error.exception),
        )

    def test_invalid_data(self):
        """Check passing invalid argspec"""

        # invalid required arguments

        for invalid_data in INVALID_DATA_1:
            with self.assertRaises(AnsibleError) as error:
                _usable_range(invalid_data)
            self.assertIn(
                "does not appear to be an IPv4 or IPv6 network",
                str(error.exception),
            )

        for invalid_data in INVALID_DATA_2:
            with self.assertRaises(AnsibleError) as error:
                _usable_range(invalid_data)
            self.assertIn("has host bits set", str(error.exception))

    def test_valid_data(self):
        """Check passing valid data as per criteria"""

        ip = VALID_DATA[0]
        result = _usable_range(ip)
        self.assertEqual(result, VALID_OUTPUT_1)

        ip = VALID_DATA[1]
        result = _usable_range(ip)
        self.assertEqual(result, VALID_OUTPUT_2)

        ip = VALID_DATA[2]
        result = _usable_range(ip)
        self.assertEqual(result, VALID_OUTPUT_3)

        ip = VALID_DATA[3]
        result = _usable_range(ip)
        self.assertEqual(result, VALID_OUTPUT_4)
