# community.general.lists_difference

* https://docs.ansible.com/ansible/latest/collections/community/general/lists_difference_filter.html

## Examples

```yaml
- name: Return the difference of list1 and list2.
  ansible.builtin.debug:
    msg: "{{ list1 | community.general.lists_difference(list2) }}"
  vars:
    list1: [1, 2, 5, 3, 4, 10]
    list2: [1, 2, 3, 4, 5, 11, 99]
```

  => [10]

```yaml
- name: Return the difference of list1, list2 and list3.
  ansible.builtin.debug:
    msg: "{{ [list1, list2, list3] | community.general.lists_difference(flatten=true) }}"
  vars:
    list1: [1, 2, 5, 3, 4, 10]
    list2: [1, 2, 3, 4, 5, 11, 99]
    list3: [1, 2, 3, 4, 5, 10, 99, 101]
```

  => []
