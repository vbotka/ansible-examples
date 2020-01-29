def dict_flatten(d, separator='.'):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + separator)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + separator)
                i += 1
        else:
            out[name[:-1]] = x
    flatten(d)
    return out

class FilterModule(object):
    def filters(self):
        return {
            'dict_flatten': dict_flatten
        }
