import random

def list_sample(l,n):
    return random.sample(l,n)

class FilterModule(object):
    def filters(self):
        return {
            'list_sample' : list_sample
        }
