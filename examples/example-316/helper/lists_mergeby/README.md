# Docs helper. Create RST file.

The playbook `playbook.yml` writes a RST file that can be used in
docs/docsite/rst. The usage of this helper is recommended but not
mandatory. You can stop reading here and update the RST file manually
if you don't want to use this helper.

## Run the playbook

If you want to generate the RST file by this helper fit the variables,
the playbook, and the template to your needs. Then, run the play

```sh
shell> ansible-playbook playbook.yml -e @extra-vars.yml  -e debug=true
```

## Copy RST to docs/docsite/rst

Copy the RST file to `docs/docsite/rst` and remove it from this
directory.
