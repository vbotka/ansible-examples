def hash_to_tuples(h):
    return h.items()

def hash_keys(h):
    return h.keys()

def hash_values(h):
    return h.values()

class FilterModule(object):
    ''' utility filters for operating on hashes '''

    def filters(self):
        return {
            'hash_to_tuples' : hash_to_tuples
            ,'hash_keys'     : hash_keys
            ,'hash_values'   : hash_values
        }
