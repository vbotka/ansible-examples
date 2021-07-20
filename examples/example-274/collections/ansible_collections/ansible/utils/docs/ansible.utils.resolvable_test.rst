.. _ansible.utils.resolvable_test:


************************
ansible.utils.resolvable
************************

**Test if an IP or name can be resolved via /etc/hosts or DNS**


Version added: 2.2.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This plugin checks if the provided IP address of host name can be resolved using /etc/hosts or DNS




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
                    <b>host</b>
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
                        <div>A string that represents the IP address or the host name</div>
                        <div>{&#x27;For example&#x27;: [&#x27;docs.ansible.com&#x27;, &#x27;127.0.0.1&#x27;, &#x27;::1&#x27;]}</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    #### Simple examples

    - name: Check if docs.ansible.com is resolvable or not
      ansible.builtin.set_fact:
        data: "{{ 'docs.ansible.com' is ansible.utils.resolvable }}"

    # TASK [Check if docs.ansible.com is resolvable or not] **********************************
    # ok: [localhost] => {
    #     "ansible_facts": {
    #         "data": true
    #     },
    #     "changed": false
    # }

    - name: Set host name variables
      ansible.builtin.set_fact:
        good_name: www.google.com
        bad_name: foo.google.com

    - name: Assert good_name's resolvability
      assert:
        that: "{{ 'www.google.com' is ansible.utils.resolvable }}"

    - name: Assert bad_name's resolvability
      assert:
        that: "{{ 'foo.google.com' is not ansible.utils.resolvable }}"

    # TASK [Assert good_name's resolvability] ************************************************
    # ok: [localhost] => {
    #     "changed": false,
    #     "msg": "All assertions passed"
    # }

    # TASK [Assert bad_name's resolvability] *************************************************
    # ok: [localhost] => {
    #     "changed": false,
    #     "msg": "All assertions passed"
    # }

    - name: Set ip variables
      ansible.builtin.set_fact:
        ipv4_localhost: "127.0.0.1"
        ipv6_localhost: "::1"

    - name: Assert ipv4_localhost's resolvability
      assert:
        that: "{{ ipv4_localhost is ansible.utils.resolvable }}"

    - name: Assert ipv6_localhost's resolvability
      assert:
        that: "{{ ipv6_localhost is ansible.utils.resolvable }}"

    # TASK [Assert ipv4_localhost's resolvability] *******************************************
    # ok: [localhost] => {
    #     "changed": false,
    #     "msg": "All assertions passed"
    # }

    # TASK [Assert ipv6_localhost's resolvability] *******************************************
    # ok: [localhost] => {
    #     "changed": false,
    #     "msg": "All assertions passed"
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
