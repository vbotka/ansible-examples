def prefix_key(d, prefix='prefix'):
    for key in d.keys():
        d[prefix + key] = d.pop(key)
    return d

class FilterModule(object):
    ''' utility filters for operating on dictionary '''

    def filters(self):
        return {
            'prefix_key' : prefix_key
        }
