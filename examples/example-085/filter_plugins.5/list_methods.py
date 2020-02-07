def list_split_period(l, p):
    split_list = []
    for i in range(p, len(l)+p, p):
        if i == p:
            split_list.append(l[0:p])
        elif i > len(l):
            split_list.append(l[j:])
        else:
            split_list.append(l[j:i])
        j = i
    return split_list

class FilterModule(object):

    def filters(self):
        return {
            'list_split_period': list_split_period
        }
