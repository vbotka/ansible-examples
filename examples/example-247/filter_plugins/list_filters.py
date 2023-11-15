def list2dict(l):
    out = []
    for i in l:
        item = {}
        for j in range(0, len(i)):
            item.update(i[j])
        out.append(item)
    return out


class FilterModule(object):
    ''' List filters. '''

    def filters(self):
        return {
            'list2dict': list2dict,
        }
