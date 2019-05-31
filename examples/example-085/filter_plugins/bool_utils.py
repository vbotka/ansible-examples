def bool_and(h):
    return all(h)
def bool_or(h):
    return any(h)
class FilterModule(object):
    ''' utility filters for operating on list of Boolean '''
    def filters(self):
        return {
            'bool_and' : bool_and,
            'bool_or' : bool_or
        }
