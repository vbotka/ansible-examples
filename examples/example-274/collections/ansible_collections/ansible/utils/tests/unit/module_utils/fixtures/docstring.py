DOCUMENTATION = """
module: test
author: Bradley Thornton (@cidrblock)
short_description: Short description here
description:
- A longer description here
version_added: 0.0.0
options:
    param_str:
        type: str
        description:
        - A string param
        required: True
    params_bool:
        type: bool
        description:
        - A bool param
    params_dict:
        type: dict
        description:
        - A dict param
        suboptions:
            subo_str:
                type: str
                description:
                - A string suboption
            subo_list:
                type: list
                description:
                - A list suboption
            subo_dict:
                type: dict
                description:
                - A dict suboption
    param_default:
        type: bool
        default: True
"""
