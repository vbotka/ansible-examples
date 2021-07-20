.. _ansible.utils.get_path_filter:


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
- Use a *path* to retrieve a nested value from a *var*.
- **get_path** is also available as a **lookup plugin** for convenience.
- Using the parameters below- ``var|ansible.utils.get_path(path, wantlist``)




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
                        <div>The <em>path</em> in the <em>var</em> to retrieve the value of.</div>
                        <div>The <em>path</em> needs to be a valid jinja path.</div>
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
                        <div>This option represents the value that is passed to the filter plugin in pipe format.</div>
                        <div>For example <code>config_data|ansible.utils.get_path(</code>), in this case <code>config_data</code> represents this option.</div>
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
                        <div>If set to <code>True</code>, the return value will always be a list.</div>
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
        value: "{{ a|ansible.utils.get_path(path) }}"
      vars:
        path: b.c.d[0]

    # TASK [Retrieve a value deep inside a using a path] ******************
    # ok: [localhost] => changed=false
    #   ansible_facts:
    #     value: '0'


    #### Working with hostvars

    - name: Retrieve a value deep inside all of the host's vars
      ansible.builtin.set_fact:
        value: "{{ look_in|ansible.utils.get_path(look_for) }}"
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
        paths: "{{ a|ansible.utils.to_paths(prepend='a') }}"

    - name: Retrieve the value of each path from vars
      ansible.builtin.debug:
        msg: "The value of path {{ path }} in vars is {{ value }}"
      loop: "{{ paths.keys()|list }}"
      loop_control:
        label: "{{ item }}"
      vars:
        path: "{{ item }}"
        value: "{{ vars|ansible.utils.get_path(item) }}"

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
        msg: "{{ rekeyed|ansible.utils.get_path(item) }}"
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




Status
------


Authors
~~~~~~~

- Bradley Thornton (@cidrblock)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
