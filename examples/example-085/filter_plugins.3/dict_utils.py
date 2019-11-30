def dict_del_key(d, key):
    del d[key]
    return d

class FilterModule(object):
    ''' Ansible filters. Interface to Python dictionary methods.'''

    def filters(self):
        return {
            'dict_del_key' : dict_del_key
        }
