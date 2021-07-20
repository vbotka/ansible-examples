.. _ansible.utils.fact_diff_module:


***********************
ansible.utils.fact_diff
***********************

**Find the difference between currently set facts**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Compare two facts or variables and get a diff.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The second fact to be used in the comparison.</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The first fact to be used in the comparison.</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>plugin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">{}</div>
                </td>
                <td>
                        <div>Configure and specify the diff plugin to use</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"ansible.utils.native"</div>
                </td>
                <td>
                        <div>The diff plugin to use, in fully qualified collection name format.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vars</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">{}</div>
                </td>
                <td>
                        <div>Parameters passed to the diff plugin.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>skip_lines</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Skip lines matching these regular expressions.</div>
                        <div>Matches will be removed prior to the diff.</div>
                        <div>If the provided <em>before</em> and <em>after</em> are a string, they will be split.</div>
                        <div>Each entry in each list will be cast to a string for the comparison</div>
                </td>
            </tr>


    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - ansible.builtin.set_fact:
        before:
          a:
            b:
              c:
                d:
                - 0
                - 1
        after:
          a:
            b:
              c:
                d:
                - 2
                - 3

    - name: Show the difference in json format
      ansible.utils.fact_diff:
        before: "{{ before }}"
        after: "{{ after }}"

    # TASK [ansible.utils.fact_diff] **************************************
    # --- before
    # +++ after
    # @@ -3,8 +3,8 @@
    #          "b": {
    #              "c": {
    #                  "d": [
    # -                    0,
    # -                    1
    # +                    2,
    # +                    3
    #                  ]
    #              }
    #          }
    #
    # changed: [localhost]

    - name: Show the difference in path format
      ansible.utils.fact_diff:
        before: "{{ before|ansible.utils.to_paths }}"
        after: "{{ after|ansible.utils.to_paths }}"

    # TASK [ansible.utils.fact_diff] **************************************
    # --- before
    # +++ after
    # @@ -1,4 +1,4 @@
    #  {
    # -    "a.b.c.d[0]": 0,
    # -    "a.b.c.d[1]": 1
    # +    "a.b.c.d[0]": 2,
    # +    "a.b.c.d[1]": 3
    #  }
    #
    # changed: [localhost]

    - name: Show the difference in yaml format
      ansible.utils.fact_diff:
        before: "{{ before|to_nice_yaml }}"
        after: "{{ after|to_nice_yaml }}"

    # TASK [ansible.utils.fact_diff] **************************************
    # --- before
    # +++ after
    # @@ -2,5 +2,5 @@
    #      b:
    #          c:
    #              d:
    # -            - 0
    # -            - 1
    # +            - 2
    # +            - 3

    # changed: [localhost]


    #### Show the difference between complex object using restconf
    #  ansible_connection: ansible.netcommon.httpapi
    #  ansible_httpapi_use_ssl: True
    #  ansible_httpapi_validate_certs: False
    #  ansible_network_os: ansible.netcommon.restconf

    - name: Get the current interface config prior to changes
      ansible.netcommon.restconf_get:
        content: config
        path: /data/Cisco-NX-OS-device:System/intf-items/phys-items
      register: pre

    - name: Update the description of eth1/100
      ansible.utils.update_fact:
        updates:
        - path: "pre['response']['phys-items']['PhysIf-list'][{{ index }}]['descr']"
          value: "Configured by ansible {{ 100 | random }}"
      vars:
        index: "{{ pre['response']['phys-items']['PhysIf-list']|ansible.utils.index_of('eq', 'eth1/100', 'id') }}"
      register: updated

    - name: Apply the configuration
      ansible.netcommon.restconf_config:
        path: 'data/Cisco-NX-OS-device:System/intf-items/'
        content: "{{ updated.pre.response}}"
        method: patch

    - name: Get the current interface config after changes
      ansible.netcommon.restconf_get:
        content: config
        path: /data/Cisco-NX-OS-device:System/intf-items/phys-items
      register: post

    - name: Show the difference
      ansible.utils.fact_diff:
        before: "{{ pre.response|ansible.utils.to_paths }}"
        after: "{{ post.response|ansible.utils.to_paths }}"

    # TASK [ansible.utils.fact_diff] *********************************************
    # --- before
    # +++ after
    # @@ -3604,7 +3604,7 @@
    #      "phys-items['PhysIf-list'][37].bw": "0",
    #      "phys-items['PhysIf-list'][37].controllerId": "",
    #      "phys-items['PhysIf-list'][37].delay": "1",
    # -    "phys-items['PhysIf-list'][37].descr": "Configured by ansible 95",
    # +    "phys-items['PhysIf-list'][37].descr": "Configured by ansible 20",
    #      "phys-items['PhysIf-list'][37].dot1qEtherType": "0x8100",
    #      "phys-items['PhysIf-list'][37].duplex": "auto",
    #      "phys-items['PhysIf-list'][37].id": "eth1/100",

    # changed: [nxos101]



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>diff_lines</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The <em>diff_text</em> split into lines.</div>
                    <br/>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>diff_text</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The diff in text format.</div>
                    <br/>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Bradley Thornton (@cidrblock)
