#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#


"""
The to_xml filter plugin
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: to_xml
    author: Ashwini Mhatre (@amhatre)
    version_added: "2.0.2"
    short_description: Convert given JSON string to XML
    description:
        - This plugin converts the JSON string to XML.
        - Using the parameters below- C(data|ansible.utils.to_xml)
    options:
      data:
        description:
        - The input JSON string .
        - This option represents the JSON value that is passed to the filter plugin in pipe format.
        - For example C(config_data|ansible.utils.to_xml), in this case C(config_data) represents this option.
        type: dict
        required: True
      engine:
        description:
        - Conversion library to use within the filter plugin.
        type: str
        default: xmltodict
"""

EXAMPLES = r"""

#### Simple examples with out any engine. plugin will use default value as xmltodict

- name: Define JSON data
  ansible.builtin.set_fact:
      data:
        "interface-configurations":
          "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"
          "interface-configuration":
- debug:
    msg:  "{{ data|ansible.utils.to_xml }}"

# TASK [Define JSON data ] *************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:5
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": {
#             "interface-configurations": {
#                 "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
#                 "interface-configuration": null
#             }
#         }
#     },
#     "changed": false
# }
#
# TASK [debug] ***********************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:13
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<interface-configurations xmlns=\"http://cisco.com/ns/yang/
#     Cisco-IOS-XR-ifmgr-cfg\">\n\t<interface-configuration></interface-configuration>\n</interface-configurations>"
# }

#### example2 with engine=xmltodict

- name: Define JSON data
  ansible.builtin.set_fact:
    data:
      "interface-configurations":
          "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"
          "interface-configuration":
- debug:
    msg:  "{{ data|ansible.utils.to_xml('xmltodict') }}"

# TASK [Define JSON data ] *************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:5
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": {
#             "interface-configurations": {
#                 "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
#                 "interface-configuration": null
#             }
#         }
#     },
#     "changed": false
# }
# TASK [debug] ***********************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:13
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<interface-configurations xmlns=\"http://cisco.com/ns/yang/
#     Cisco-IOS-XR-ifmgr-cfg\">\n\t<interface-configuration></interface-configuration>\n</interface-configurations>"
# }

"""

from ansible.errors import AnsibleFilterError
from jinja2.filters import environmentfilter
from ansible_collections.ansible.utils.plugins.plugin_utils.to_xml import (
    to_xml,
)
from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
    AnsibleArgSpecValidator,
)


@environmentfilter
def _to_xml(*args, **kwargs):
    """Convert the given data from json to xml."""
    keys = ["data", "engine"]
    data = dict(zip(keys, args[1:]))
    data.update(kwargs)
    aav = AnsibleArgSpecValidator(
        data=data, schema=DOCUMENTATION, name="to_xml"
    )
    valid, errors, updated_data = aav.validate()
    if not valid:
        raise AnsibleFilterError(errors)
    return to_xml(**updated_data)


class FilterModule(object):
    """ to_xml  """

    def filters(self):
        """a mapping of filter names to functions"""
        return {"to_xml": _to_xml}
