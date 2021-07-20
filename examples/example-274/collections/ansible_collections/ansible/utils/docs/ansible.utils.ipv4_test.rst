.. _ansible.utils.ipv4_test:


******************
ansible.utils.ipv4
******************

**Test if something is an IPv4 address or network**


Version added: 2.2.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This plugin checks if the provided value is a valid host or network IP address with IPv4 addressing scheme




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
                    <b>ip</b>
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
                        <div>A string that represents the value against which the test is going to be performed</div>
                        <div>{&#x27;For example&#x27;: [&#x27;10.1.1.1&#x27;, &#x27;10.0.0.0/8&#x27;, &#x27;fe80::216:3eff:fee4:16f3&#x27;]}</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    #### Simple examples

    - name: Check if 10.0.0.0/8 is a valid IPv4 address
      ansible.builtin.set_fact:
        data: "{{ '10.0.0.0/8' is ansible.utils.ipv4 }}"

    # TASK [Check if 10.0.0.0/8 is a valid IPv4 address] ***************************
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": true
    #     },
    #     "changed": false
    # }

    - name: Check if 192.168.1.250 is a valid IPv4 address
      ansible.builtin.set_fact:
        data: "{{ '192.168.1.250' is ansible.utils.ipv4 }}"

    # TASK [Check if 192.168.1.250 is a valid IPv4 address] ********************
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": true
    #     },
    #     "changed": false
    # }

    - name: Check if fe80::216:3eff:fee4:16f3 is not a valid IPv4 address
      ansible.builtin.set_fact:
        data: "{{ 'fe80::216:3eff:fee4:16f3' is not ansible.utils.ipv4 }}"

    # TASK [Check if fe80::216:3eff:fee4:16f3 is not a valid IPv4 address] *********
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": true
    #     },
    #     "changed": false
    # }



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this test:

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
                    <b>data</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">-</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>If jinja test satisfies plugin expression <code>true</code></div>
                            <div>If jinja test does not satisfy plugin expression <code>false</code></div>
                    <br/>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Priyam Sahoo (@priyamsahoo)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
