def custom_1(h):
    return {'key3': sum(h.values())}

def dict_merge(x, y, recursive=False):
    if recursive:
        z = dict(list(x.items()) + list(y.items()))
    else:
        z = x.copy()
        z.update(y)
    return z

def dict_keys(d):
    return list(d)


class FilterModule(object):

    def filters(self):
        return {
            'custom_1' : custom_1,
            'dict_keys' : dict_keys,
            'dict_merge' : dict_merge,
        }
