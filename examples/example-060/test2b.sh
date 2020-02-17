#!/bin/sh
cat $1 | jq ".ansible_facts.packages.$2[].version"

# Ansible output extract package version using jq
# https://stackoverflow.com/questions/60228560/ansible-output-extract-package-version-using-jq/
# 
# Q: "How can I use jq to get the version number for matching package
#     name?"
# 
# A: Try the script below
# 
# $ cat print-version.sh
# #!/bin/sh
# cat output.json | jq ".ansible_facts.packages.$1 | .[].version"
# 
# For example
# 
# $ print-version.sh GeoIP
# "1.5.0"
# 
# Improved version of the script
# 
# Quoting the comment: "Using the shell's string interpolation as done
# here is risky and generally regarded as an "anti-pattern". – peak"
# 
# The improved script below does the job
# 
# $ cat print-version.sh
# #!/bin/sh
# cat output.json | jq ".ansible_facts.packages.$1[].version"
