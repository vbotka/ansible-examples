def dict_merge_lossless(x, y):
    d = x.copy()
    d.update(y)
    for key, value in d.items():
       if key in x and key in y:
               d[key] = [value , x[key]]
    return d

class FilterModule(object):
    ''' Ansible filters. Interface to Python dictionary methods.'''

    def filters(self):
        return {
            'dict_merge_lossless' : dict_merge_lossless
        }
