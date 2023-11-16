from fqdn import FQDN


def fqdn_valid(host, min_labels=1, allow_underscores=False):
    f = FQDN(host,
             min_labels=min_labels,
             allow_underscores=allow_underscores)
    return(f.is_valid)


class TestModule(object):
    ''' Ansible test hostnames.
        https://pypi.org/project/fqdn/
    '''

    def tests(self):
        return {
            'fqdn_valid': fqdn_valid,
        }
