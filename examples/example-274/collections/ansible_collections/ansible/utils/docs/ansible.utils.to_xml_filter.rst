.. _ansible.utils.to_xml_filter:


********************
ansible.utils.to_xml
********************

**Convert given JSON string to XML**


Version added: 2.0.2

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This plugin converts the JSON string to XML.
- Using the parameters below- ``data|ansible.utils.to_xml``




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                <th>Configuration</th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>data</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                    </td>
                <td>
                        <div>The input JSON string .</div>
                        <div>This option represents the JSON value that is passed to the filter plugin in pipe format.</div>
                        <div>For example <code>config_data|ansible.utils.to_xml</code>, in this case <code>config_data</code> represents this option.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>engine</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"xmltodict"</div>
                </td>
                    <td>
                    </td>
                <td>
                        <div>Conversion library to use within the filter plugin.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

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




Status
------


Authors
~~~~~~~

- Ashwini Mhatre (@amhatre)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
