# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    author: Ganesh Nalawade (@ganeshrn)
    name: jsonschema
    short_description: Define configurable options for jsonschema validate plugin
    description:
    - This sub plugin documentation provides the configurable options that can be passed
      to the validate plugins when C(ansible.utils.jsonschema) is used as a value for
      engine option.
    version_added: 1.0.0
    options:
      draft:
        description:
        - This option provides the jsonschema specification that should be used
          for the validating the data. The I(criteria) option in the validate
          plugin should follow the specification as mentioned by this option
        default: draft7
        choices:
        - draft3
        - draft4
        - draft6
        - draft7
        env:
        - name: ANSIBLE_VALIDATE_JSONSCHEMA_DRAFT
        vars:
        - name: ansible_validate_jsonschema_draft
    notes:
    - The value of I(data) option should be either a valid B(JSON) object or a B(JSON) string.
    - The value of I(criteria) should be B(list) of B(dict) or B(list) of B(strings) and each
      B(string) within the B(list) entry should be a valid B(dict) when read in python.
"""

import json

from ansible.module_utils._text import to_text
from ansible.module_utils.basic import missing_required_lib
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types

from ansible_collections.ansible.utils.plugins.plugin_utils.base.validate import (
    ValidateBase,
)

from ansible_collections.ansible.utils.plugins.module_utils.common.utils import (
    to_list,
)

# PY2 compatiblilty for JSONDecodeError
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

try:
    import jsonschema

    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


def to_path(fpath):
    return ".".join(str(index) for index in fpath)


def json_path(absolute_path):
    path = "$"
    for elem in absolute_path:
        if isinstance(elem, int):
            path += "[" + str(elem) + "]"
        else:
            path += "." + elem
    return path


class Validate(ValidateBase):
    @staticmethod
    def _check_reqs():
        """Check the prerequisites are installed for jsonschema

        :return None: In case all prerequisites are satisfised
        """
        if not HAS_JSONSCHEMA:
            raise AnsibleError(missing_required_lib("jsonschema"))

    def _check_args(self):
        """Ensure specific args are set

        :return: None: In case all arguments passed are valid
        """
        try:
            if isinstance(self._data, string_types):
                self._data = json.loads(self._data)
            else:
                self._data = json.loads(json.dumps(self._data))

        except (TypeError, JSONDecodeError) as exe:
            msg = (
                "'data' option value is invalid, value should a valid JSON."
                " Failed to read with error '{err}'".format(
                    err=to_text(exe, errors="surrogate_then_replace")
                )
            )
            raise AnsibleError(msg)

        try:
            criteria = []
            for item in to_list(self._criteria):
                if isinstance(self._criteria, string_types):
                    criteria.append(json.loads(item))
                else:
                    criteria.append(json.loads(json.dumps(item)))

            self._criteria = criteria
        except (TypeError, JSONDecodeError) as exe:
            msg = (
                "'criteria' option value is invalid, value should a valid JSON."
                " Failed to read with error '{err}'".format(
                    err=to_text(exe, errors="surrogate_then_replace")
                )
            )
            raise AnsibleError(msg)

    def validate(self):
        """Std entry point for a validate execution

        :return: Errors or parsed text as structured data
        :rtype: dict

        :example:

        The parse function of a parser should return a dict:
        {"errors": [a list of errors]}
        or
        {"parsed": obj}
        """
        self._check_reqs()
        self._check_args()

        try:
            self._validate_jsonschema()
        except Exception as exc:
            return {"errors": to_text(exc, errors="surrogate_then_replace")}

        return self._result

    def _validate_jsonschema(self):
        error_messages = None

        draft = self._get_sub_plugin_options("draft")
        error_messages = []

        for criteria in self._criteria:
            if draft == "draft3":
                validator = jsonschema.Draft3Validator(criteria)
            elif draft == "draft4":
                validator = jsonschema.Draft4Validator(criteria)
            elif draft == "draft6":
                validator = jsonschema.Draft6Validator(criteria)
            else:
                validator = jsonschema.Draft7Validator(criteria)

            validation_errors = sorted(
                validator.iter_errors(self._data), key=lambda e: e.path
            )

            if validation_errors:
                if "errors" not in self._result:
                    self._result["errors"] = []

                for validation_error in validation_errors:
                    if isinstance(
                        validation_error, jsonschema.ValidationError
                    ):
                        error = {
                            "message": validation_error.message,
                            "data_path": to_path(
                                validation_error.absolute_path
                            ),
                            "json_path": json_path(
                                validation_error.absolute_path
                            ),
                            "schema_path": to_path(
                                validation_error.relative_schema_path
                            ),
                            "relative_schema": validation_error.schema,
                            "expected": validation_error.validator_value,
                            "validator": validation_error.validator,
                            "found": validation_error.instance,
                        }
                        self._result["errors"].append(error)
                        error_message = "At '{schema_path}' {message}. ".format(
                            schema_path=error["schema_path"],
                            message=error["message"],
                        )
                        error_messages.append(error_message)
        if error_messages:
            if "msg" not in self._result:
                self._result["msg"] = "\n".join(error_messages)
            else:
                self._result["msg"] += "\n".join(error_messages)
