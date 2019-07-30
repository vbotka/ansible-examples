def dict_add_hash(d, h):
    for k, v in h.iteritems():
        d[k] = v
    return d

class FilterModule(object):
    ''' Ansible filters. Interface to Python dictionary methods.'''

    def filters(self):
        return {
            'dict_add_hash' : dict_add_hash
        }
