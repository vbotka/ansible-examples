.. _ansible.utils.validate_lookup:


**********************
ansible.utils.validate
**********************

**Validate data with provided criteria**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Validate *data* with provided *criteria* based on the validation *engine*.




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
                    <b>criteria</b>
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
                        <div>The criteria used for validation of value that represents <em>data</em> options.</div>
                        <div>This option represents the second argument passed in the lookup plugin For example <code>lookup(config_data, config_criteria, engine=&#x27;ansible.utils.jsonschema&#x27;</code>), in this case the value of <code>config_criteria</code> represents this option.</div>
                        <div>For the type of <em>criteria</em> that represents this value refer to the documentation of individual validate plugins.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>data</b>
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
                        <div>Data that will be validated against <em>criteria</em>.</div>
                        <div>This option represents the value that is passed to the lookup plugin as the first argument. For example <code>lookup(config_data, config_criteria, engine=&#x27;ansible.utils.jsonschema&#x27;</code>), in this case <code>config_data</code> represents this option.</div>
                        <div>For the type of <em>data</em> that represents this value refer to the documentation of individual validate plugins.</div>
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
                        <b>Default:</b><br/><div style="color: blue">"ansible.utils.jsonschema"</div>
                </td>
                    <td>
                    </td>
                <td>
                        <div>The name of the validate plugin to use.</div>
                        <div>This option can be passed in lookup plugin as a key, value pair. For example <code>lookup(config_data, config_criteria, engine=&#x27;ansible.utils.jsonschema&#x27;</code>), in this case the value <code>ansible.utils.jsonschema</code> represents the engine to be use for data validation. If the value is not provided the default value that is <code>ansible.uitls.jsonschema</code> will be used.</div>
                        <div>The value should be in fully qualified collection name format that is <code>&lt;org-name&gt;.&lt;collection-name&gt;.&lt;validate-plugin-name&gt;</code>.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - For the type of options *data* and *criteria* refer to the individual validate plugin documentation that is represented in the value of *engine* option.
   - For additional plugin configuration options refer to the individual validate plugin documentation that is represented by the value of *engine* option.
   - The plugin configuration option can be either passed as ``key=value`` pairs within lookup plugin or task or environment variables.
   - The precedence the validate plugin configurable option is the variable passed within lookup plugin as ``key=value`` pairs followed by task variables followed by environment variables.



Examples
--------

.. code-block:: yaml

    - name: set facts for data and criteria
      ansible.builtin.set_fact:
        data: "{{ lookup('ansible.builtin.file', './validate/data/show_interfaces_iosxr.json')}}"
        criteria: "{{ lookup('ansible.builtin.file', './validate/criteria/jsonschema/show_interfaces_iosxr.json')}}"

    - name: validate data in json format using jsonschema with lookup plugin by passing plugin configuration variable as key/value pairs
      ansible.builtin.set_fact:
        data_criteria_checks: "{{ lookup(data, criteria, engine='ansible.utils.jsonschema', draft='draft7') }}"

    - name: validate data in json format using jsonschema with lookup plugin by passing plugin configuration variable as task variable
      ansible.builtin.set_fact:
        data_criteria_checks: "{{ lookup('ansible.utils.validate', data, criteria, engine='ansible.utils.jsonschema', draft='draft7') }}"
      vars:
        ansible_validate_jsonschema_draft: draft3



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
                            <div>If data is valid returns empty list.</div>
                            <div>If data is invalid returns list of errors in data.</div>
                    <br/>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
