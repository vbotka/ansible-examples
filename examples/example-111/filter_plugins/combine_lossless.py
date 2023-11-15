def combine_lossless(x, y, flatten=False, unique=False):
    d = x.copy()
    d.update(y)
    for key, value in d.items():
        if key in x and key in y:
            if flatten and isinstance(value, list) and isinstance(x[key], list):
                if unique:
                    d[key] = list(set(value + x[key]))
                else:
                    d[key] = value + x[key]
            else:
                if unique:
                    d[key] = list(set([value, x[key]]))
                else:
                    d[key] = [value, x[key]]
    return d


class FilterModule(object):
    ''' Ansible filters. '''

    def filters(self):
        return {
            'combine_lossless': combine_lossless,
}
