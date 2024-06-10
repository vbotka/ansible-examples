Contribute to a collection docsite
==================================
https://ansible.readthedocs.io/projects/antsibull-docs/collection-docs/


Set up development for a collection
-----------------------------------
https://ansible.readthedocs.io/projects/antsibull-docs/collection-docs/#setting-up-development-for-a-collection

```bash
shell> python3 -m venv ~/antsibull-demo-venv
  ...
```


Create rst file
---------------

```bash
shell> cd ansible.community.general/docs/docsite/helper/lists_mergeby
shell> ansible-playbook playbook.yml -e @extra-vars.yml
```

Copy rst file from helper to docsite

```bash
shell> cp *.rst ../../rst
```

Building a docsite
------------------

```bash
shell> . ~/antsibull-demo-venv/bin/activate
(antsibull-demo-venv) > mkdir ~/built-docs
(antsibull-demo-venv) > chmod g-w ~/built-docs
(antsibull-demo-venv) > python3 -m pip install ansible-core antsibull-docs
(antsibull-demo-venv) > export ANSIBLE_COLLECTIONS_PATH=/scratch/collections
(antsibull-demo-venv) > antsibull-docs sphinx-init --use-current --squash-hierarchy community.general --dest-dir built-docs
(antsibull-demo-venv) > cd ~/built-docs
(antsibull-demo-venv) > python3 -m pip install -r requirements.txt
(antsibull-demo-venv) > ./build.sh
```

Open in browser file:///home/vlado/built-docs/build/html/index.html
