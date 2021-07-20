.. _ansible.utils.usable_range_filter:


**************************
ansible.utils.usable_range
**************************

**Expand the usable IP addresses**


Version added: 2.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- For a given IP address (IPv4 or IPv6) in CIDR form, the plugin generates a list of usable IP addresses belonging to the network.




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
                        <div>A string that represents an IP address of network in CIDR form</div>
                        <div>{&#x27;For example&#x27;: [&#x27;10.0.0.0/24&#x27;, &#x27;2001:db8:abcd:0012::0/124&#x27;]}</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    #### Simple examples

    - name: Expand and produce list of usable IP addresses in 10.0.0.0/28
      ansible.builtin.set_fact:
        data: "{{ '10.0.0.0/28' | ansible.utils.usable_range }}"

    # TASK [Expand and produce list of usable IP addresses in 10.0.0.0/28] ************************
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": {
    #             "number_of_ips": 16,
    #             "usable_ips": [
    #                 "10.0.0.0",
    #                 "10.0.0.1",
    #                 "10.0.0.2",
    #                 "10.0.0.3",
    #                 "10.0.0.4",
    #                 "10.0.0.5",
    #                 "10.0.0.6",
    #                 "10.0.0.7",
    #                 "10.0.0.8",
    #                 "10.0.0.9",
    #                 "10.0.0.10",
    #                 "10.0.0.11",
    #                 "10.0.0.12",
    #                 "10.0.0.13",
    #                 "10.0.0.14",
    #                 "10.0.0.15"
    #             ]
    #         }
    #     },
    #     "changed": false
    # }

    - name: Expand and produce list of usable IP addresses in 2001:db8:abcd:0012::0/126
      ansible.builtin.set_fact:
        data1: "{{ '2001:db8:abcd:0012::0/126' | ansible.utils.usable_range }}"

    # TASK [Expand and produce list of usable IP addresses in 2001:db8:abcd:0012::0/126] ***
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data1": {
    #             "number_of_ips": 4,
    #             "usable_ips": [
    #                 "2001:db8:abcd:12::",
    #                 "2001:db8:abcd:12::1",
    #                 "2001:db8:abcd:12::2",
    #                 "2001:db8:abcd:12::3"
    #             ]
    #         }
    #     },
    #     "changed": false
    # }

    - name: Expand and produce list of usable IP addresses in 10.1.1.1
      ansible.builtin.set_fact:
        data: "{{ '10.1.1.1' | ansible.utils.usable_range }}"

    # TASK [Expand and produce list of usable IP addresses in 10.1.1.1] ***************************
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": {
    #             "number_of_ips": 1,
    #             "usable_ips": [
    #                 "10.1.1.1"
    #             ]
    #         }
    #     },
    #     "changed": false
    # }

    #### Simple Use-case (looping through the list result)

    - name: Expand and produce list of usable IP addresses in 127.0.0.0/28
      ansible.builtin.set_fact:
        data1: "{{ '127.0.0.0/28' | ansible.utils.usable_range }}"

    - name: Ping all but first IP addresses from the generated list
      shell: "ping -c 1 {{ item }}"
      loop: "{{ data1.usable_ips[1:] }}"

    # TASK [Expand and produce list of usable IP addresses in 127.0.0.0/28] ******************************
    # ok: [localhost]

    # TASK [Ping all but first IP addresses from the generated list] *************************************
    # changed: [localhost] => (item=127.0.0.1)
    # changed: [localhost] => (item=127.0.0.2)
    # changed: [localhost] => (item=127.0.0.3)
    # changed: [localhost] => (item=127.0.0.4)
    # changed: [localhost] => (item=127.0.0.5)
    # changed: [localhost] => (item=127.0.0.6)
    # changed: [localhost] => (item=127.0.0.7)
    # changed: [localhost] => (item=127.0.0.8)
    # changed: [localhost] => (item=127.0.0.9)
    # changed: [localhost] => (item=127.0.0.10)
    # changed: [localhost] => (item=127.0.0.11)
    # changed: [localhost] => (item=127.0.0.12)
    # changed: [localhost] => (item=127.0.0.13)
    # changed: [localhost] => (item=127.0.0.14)
    # changed: [localhost] => (item=127.0.0.15)



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this filter:

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
                            <div>Total number of usable IP addresses under the key <code>number_of_ips</code></div>
                            <div>List of usable IP addresses under the key <code>usable_ips</code></div>
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
