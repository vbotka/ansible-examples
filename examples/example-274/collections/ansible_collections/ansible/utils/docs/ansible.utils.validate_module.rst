.. _ansible.utils.validate_module:


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
- Validate data with provided criteria based on the validation engine.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
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
                        <div>The criteria used for validation of <em>data</em>. For the type of criteria refer to the documentation of individual validate plugins.</div>
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
                        <div>Data that will be validated against <em>criteria</em>. For the type of data refer to the documentation of individual validate plugins.</div>
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
                        <div>The name of the validate plugin to use. The engine value should follow the fully qualified collection name format, that is &lt;org-name&gt;.&lt;collection-name&gt;.&lt;validate-plugin-name&gt;.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - For the type of options *data* and *criteria* refer to the individual validate plugin documentation that is represented in the value of *engine* option.
   - For additional plugin configuration options refer to the individual validate plugin documentation that is represented by the value of *engine* option.
   - The plugin configuration option can be either passed as task or environment variables.
   - The precedence of the validate plugin configurable option is task variables followed by the environment variables.



Examples
--------

.. code-block:: yaml

    - name: set facts for data and criteria
      ansible.builtin.set_fact:
        data: "{{ lookup('ansible.builtin.file', './validate/data/show_interfaces_iosxr.json')}}"
        criteria: "{{ lookup('ansible.builtin.file', './validate/criteria/jsonschema/show_interfaces_iosxr.json')}}"

    - name: validate data in with jsonschema engine (by passing task vars as configurable plugin options)
      ansible.utils.validate:
        data: "{{ data }}"
        criteria: "{{ criteria }}"
        engine: ansible.utils.jsonschema
      vars:
        ansible_jsonschema_draft: draft7



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
                    <b>errors</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>when <em>data</em> value is invalid</td>
                <td>
                            <div>The list of errors in <em>data</em> based on the <em>criteria</em>.</div>
                    <br/>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>msg</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The msg indicates if the <em>data</em> is valid as per the <em>criteria</em>.</div>
                            <div>In case data is valid return success message <b>all checks passed</b>.</div>
                            <div>In case data is invalid return error message <b>Validation errors were found</b> along with more information on error is available.</div>
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
- Ganesh Nalawade (@ganeshrn)
