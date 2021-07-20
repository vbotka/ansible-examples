.. _ansible.utils.get_path_lookup:


**********************
ansible.utils.get_path
**********************

**Retrieve the value in a variable using a path**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Use a *path* to retrieve a nested value from a *var*
- **get_path** is also available as a **filter plugin** for convenience
- Using the parameters below- ``lookup('ansible.utils.get_path', var, path, wantlist``)




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
                    <b>path</b>
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
                        <div>The <em>path</em> in the <em>var</em> to retrieve the value of. The <em>path</em> needs to a be a valid jinja path.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>var</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                    </td>
                <td>
                        <div>The variable from which the value should be extracted.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wantlist</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                    <td>
                    </td>
                <td>
                        <div>If set to <code>True</code>, the return value will always be a list. This can also be accomplished using <code>query</code> or <code>q</code> instead of <code>lookup</code>. <a href='https://docs.ansible.com/ansible/latest/plugins/lookup.html'>https://docs.ansible.com/ansible/latest/plugins/lookup.html</a>.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - ansible.builtin.set_fact:
        a:
          b:
            c:
              d:
              - 0
              - 1
              e:
              - True
              - False

    - name: Retrieve a value deep inside a using a path
      ansible.builtin.set_fact:
        value: "{{ lookup('ansible.utils.get_path', a, path) }}"
      vars:
        path: b.c.d[0]

    # TASK [Retrieve a value deep inside a using a path] ******************
    # ok: [localhost] => changed=false
    #   ansible_facts:
    #     value: '0'


    #### Working with hostvars

    - name: Retrieve a value deep inside all of the host's vars
      ansible.builtin.set_fact:
        value: "{{ lookup('ansible.utils.get_path', look_in, look_for) }}"
      vars:
        look_in: "{{ hostvars[inventory_hostname] }}"
        look_for: a.b.c.d[0]

    # TASK [Retrieve a value deep inside all of the host's vars] ********
    # ok: [nxos101] => changed=false
    #   ansible_facts:
    #     as_filter: '0'
    #     as_lookup: '0'


    #### Used alongside ansible.utils.to_paths

    - name: Get the paths for the object
      ansible.builtin.set_fact:
        paths: "{{ lookup('ansible.utils.to_paths', a, prepend='a') }}"

    - name: Retrieve the value of each path from vars
      ansible.builtin.debug:
        msg: "The value of path {{ path }} in vars is {{ value }}"
      loop: "{{ paths.keys()|list }}"
      loop_control:
        label: "{{ item }}"
      vars:
        path: "{{ item }}"
        value: "{{ lookup('ansible.utils.get_path', hostvars[inventory_hostname], item) }}"

    # TASK [Get the paths for the object] *******************************
    # ok: [nxos101] => changed=false
    #   ansible_facts:
    #     paths:
    #       a.b.c.d[0]: 0
    #       a.b.c.d[1]: 1
    #       a.b.c.e[0]: True
    #       a.b.c.e[1]: False

    # TASK [Retrieve the value of each path from vars] ******************
    # ok: [nxos101] => (item=a.b.c.d[0]) =>
    #   msg: The value of path a.b.c.d[0] in vars is 0
    # ok: [nxos101] => (item=a.b.c.d[1]) =>
    #   msg: The value of path a.b.c.d[1] in vars is 1
    # ok: [nxos101] => (item=a.b.c.e[0]) =>
    #   msg: The value of path a.b.c.e[0] in vars is True
    # ok: [nxos101] => (item=a.b.c.e[1]) =>
    #   msg: The value of path a.b.c.e[1] in vars is False


    #### Working with complex structures and transforming results

    - name: Retrieve the current interface config
      cisco.nxos.nxos_interfaces:
        state: gathered
      register: interfaces

    - name: Get the description of several interfaces
      ansible.builtin.debug:
        msg: "{{ lookup('ansible.utils.get_path', rekeyed, item) }}"
      vars:
        rekeyed:
          by_name: "{{ interfaces.gathered|ansible.builtin.rekey_on_member('name') }}"
      loop:
      - by_name['Ethernet1/1'].description
      - by_name['Ethernet1/2'].description|upper
      - by_name['Ethernet1/3'].description|default('')


    # TASK [Get the description of several interfaces] ******************
    # ok: [nxos101] => (item=by_name['Ethernet1/1'].description) => changed=false
    #   msg: Configured by ansible
    # ok: [nxos101] => (item=by_name['Ethernet1/2'].description|upper) => changed=false
    #   msg: CONFIGURED BY ANSIBLE
    # ok: [nxos101] => (item=by_name['Ethernet1/3'].description|default('')) => changed=false
    #   msg: ''



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this lookup:

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
                    <b>_raw</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">-</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>One or more zero-based indices of the matching list items.</div>
                            <div>See <code>wantlist</code> if a list is always required.</div>
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


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
