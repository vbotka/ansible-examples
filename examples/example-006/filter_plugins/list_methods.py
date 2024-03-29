# (c) 2019, Vladimir Botka <vbotka@gmail.com>
# All rights reserved.
# Simplified BSD License

# Get current version from
# https://github.com/vbotka/ansible-plugins/tree/master/filter_plugins


def list_append(l, x=''):
    l.append(x)
    return l


def list_extend(l, x=[]):
    l.extend(x)
    return l


def list_insert(l, i=0, x=''):
    l.insert(i, x)
    return l


def list_remove(l, x=''):
    l.remove(x)
    return l


def list_pop(l, *i):
    if len(i) == 0:
        return l.pop()
    else:
        return l.pop(i[0])


def list_clear(l):
    # l.clear()  # 'list' object has no attribute 'clear'
    del l[:]
    return l


def list_index(l, x, *i):
    if len(i) == 0:
        return l.index(x) if x in l else -1
    elif len(i) == 1:
        return l.index(x, i[0]) if x in l[i[0]:] else -1
    else:
        return l.index(x, i[0], i[1]) if x in l[i[0]:i[1]] else -1


def list_count(l, x):
    return l.count(x)


def list_sort(l, my_key=None, my_reverse=False):
    l.sort(key=my_key, reverse=my_reverse)
    return l


def list_reverse(l):
    l.reverse()
    return l


def list_copy(l):
    # l.copy()  # 'list' object has no attribute 'copy'
    return l[:]


class FilterModule(object):
    ''' Ansible filters. Interface to Python list methods.

        5.1. More on Lists
        https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        Methods of list objects.'''

    def filters(self):
        return {
            'list_append': list_append,
            'list_extend': list_extend,
            'list_insert': list_insert,
            'list_remove': list_remove,
            'list_pop': list_pop,
            'list_clear': list_clear,
            'list_index': list_index,
            'list_count': list_count,
            'list_sort': list_sort,
            'list_reverse': list_reverse,
            'list_copy': list_copy
        }
