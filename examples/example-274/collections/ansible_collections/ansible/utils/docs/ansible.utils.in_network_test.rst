.. _ansible.utils.in_network_test:


************************
ansible.utils.in_network
************************

**Test if IP address falls in the network**


Version added: 2.2.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This plugin checks if the provided IP address belongs to the provided network




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
                        <div>A string that represents an IP address</div>
                        <div>{&#x27;For example&#x27;: &#x27;10.1.1.1&#x27;}</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network</b>
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
                        <div>A string that represents the network address in CIDR form</div>
                        <div>{&#x27;For example&#x27;: &#x27;10.0.0.0/8&#x27;}</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    #### Simple examples

    - name: Check if 10.1.1.1 is in 10.0.0.0/8
      ansible.builtin.set_fact:
        data: "{{ '10.1.1.1' is ansible.utils.in_network '10.0.0.0/8' }}"

    # TASK [Check if 10.1.1.1 is in 10.0.0.0/8] ***********************************
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": true
    #     },
    #     "changed": false
    # }

    - name: Check if 10.1.1.1 is not in 192.168.1.0/24
      ansible.builtin.set_fact:
        data: "{{ '10.1.1.1' is not ansible.utils.in_network '192.168.1.0/24' }}"

    # TASK [Check if 10.1.1.1 is not in 192.168.1.0/24] ****************************
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": true
    #     },
    #     "changed": false
    # }

    - name: Check if 2001:db8:a::123 is in 2001:db8:a::/64
      ansible.builtin.set_fact:
        data: "{{ '2001:db8:a::123' is ansible.utils.in_network '2001:db8:a::/64' }}"

    # TASK [Check if 2001:db8:a::123 is in 2001:db8:a::/64] ****************************
    # task path: /home/prsahoo/playbooks/collections/localhost_test/utils_in_network.yml:16
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": true
    #     },
    #     "changed": false
    # }

    - name: Check if 2001:db8:a::123 is not in 10.0.0.0/8
      ansible.builtin.set_fact:
        data: "{{ '2001:db8:a::123' is not ansible.utils.in_network '10.0.0.0/8' }}"

    # TASK [Check if 2001:db8:a::123 is not in 10.0.0.0/8] *********************************
    # task path: /home/prsahoo/playbooks/collections/localhost_test/utils_in_network.yml:20
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
