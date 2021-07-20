.. _ansible.utils.from_xml_filter:


**********************
ansible.utils.from_xml
**********************

**Convert given XML string to native python dictionary.**


Version added: 2.0.2

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This plugin converts the XML string to a native python dictionary.
- Using the parameters below- ``data|ansible.utils.from_xml``




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
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                    </td>
                <td>
                        <div>The input XML string.</div>
                        <div>This option represents the XML value that is passed to the filter plugin in pipe format.</div>
                        <div>For example <code>config_data|ansible.utils.from_xml</code>, in this case <code>config_data</code> represents this option.</div>
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

    tasks:
      - name: convert given XML to native python dictionary
        ansible.builtin.set_fact:
          data: "
            <netconf-state xmlns=\"urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring\"><schemas><schema/></schemas></netconf-state>
                "

      - debug:
          msg:  "{{ data|ansible.utils.from_xml }}"

    ##TASK######
    # TASK [convert given XML to native python dictionary] *****************************************************************************************************
    # task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:5
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": " <netconf-state xmlns=\"urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring\"><schemas><schema/></schemas></netconf-state> "
    #     },
    #     "changed": false
    # }
    #
    # TASK [debug] *************************************************************************************************************************
    # task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:13
    # Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
    # ok: [localhost] => {
    #     "msg": {
    #         "netconf-state": {
    #             "@xmlns": "urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring",
    #             "schemas": {
    #                 "schema": null
    #             }
    #         }
    #     }
    # }

    #### example2 with engine=xmltodict

    tasks:
      - name: convert given XML to native python dictionary
        ansible.builtin.set_fact:
          data: "
            <netconf-state xmlns=\"urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring\"><schemas><schema/></schemas></netconf-state>
                "

      - debug:
          msg:  "{{ data|ansible.utils.from_xml('xmltodict') }}"

    ##TASK######
    # TASK [convert given XML to native python dictionary] *****************************************************************************************************
    # task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:5
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": " <netconf-state xmlns=\"urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring\"><schemas><schema/></schemas></netconf-state> "
    #     },
    #     "changed": false
    # }
    #
    # TASK [debug] *************************************************************************************************************************
    # task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:13
    # Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
    # ok: [localhost] => {
    #     "msg": {
    #         "netconf-state": {
    #             "@xmlns": "urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring",
    #             "schemas": {
    #                 "schema": null
    #             }
    #         }
    #     }
    # }




Status
------


Authors
~~~~~~~

- Ashwini Mhatre (@amhatre)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
