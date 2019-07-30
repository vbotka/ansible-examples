# (c) 2019, Vladimir Botka <vbotka@gmail.com>
# All rights reserved.
# Simplified BSD License

def bool_and(l):
    return all(l)

def bool_or(l):
    return any(l)

class FilterModule(object):
    ''' Ansible filters for operating on list of Boolean '''

    def filters(self):
        return {
            'bool_and' : bool_and,
            'bool_or' : bool_or
        }
