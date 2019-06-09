# (c) 2019, Vladimir Botka <vbotka@gmail.com>
# All rights reserved.
# Simplified BSD License

def string_prefix(s, prefix):
    return prefix + s
def string_postfix(s, postfix):
    return s + postfix
def string_count(s, sub):
    return s.count(sub)
def string_find(s, sub):
    return s.find(sub)
class FilterModule(object):
    ''' Ansible filters. Python string methods.'''
    def filters(self):
        return {
            'string_count' : string_count,
            'string_find' : string_find,
            'string_prefix' : string_prefix,
            'string_postfix' : string_postfix
        }
