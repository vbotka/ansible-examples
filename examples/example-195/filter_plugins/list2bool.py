
def fall(l):
        return all(l)

def fany(l):
        return any(l)

class FilterModule(object):
    ''' Ansible filters for operating on Boolean '''

    def filters(self):
        return {
            'fall': fall,
            'fany': fany,
            }
