from pandas.io.json import json_normalize


def dict_normalize(d):
    df = json_normalize(d)
    ll = [df.columns.values.tolist()] + df.values.tolist()
    return(ll)


class FilterModule(object):
    def filters(self):
        return {
            'dict_normalize': dict_normalize,
        }
