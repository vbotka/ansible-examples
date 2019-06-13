from distutils.version import LooseVersion


def filter_sort_versions(value):
    return sorted(value, key=LooseVersion)


class FilterModule(object):
    filter_sort = {
        'sort_versions': filter_sort_versions,
        }

    def filters(self):
        return self.filter_sort
