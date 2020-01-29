#
# Copyright 2019 Vladimir Botka <vbotka@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

# import list_methods
import sys
import json

def list_flatten(l):
    flat_list = []
    for sublist in l:
        if isinstance(sublist, (list,)):
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    l = flat_list
    return l

def dict_merge(x, y):
    d = x.copy()
    d.update(y)
    return d

def dict_add_hash(d, h, recursive=False):
    if recursive:
        for k, v in h.iteritems():
            d[k] = [d[k],v]
    else:
        for k, v in h.iteritems():
            d[k] = v
    if isinstance(d[k], (list,)):
        d[k] = list_flatten(d[k])
    return d

def dict_del_key(d, key):
    del d[key]
    return d

def dict_keys(d):
    return list(d)

def dict_sorted(d):
    return sorted(d)

def dict_search_key(d, key):
    return key in d

def dict_prefix_keys(d, prefix='prefix_'):
    for key in d.keys():
        d[prefix + key] = d.pop(key)
    return d

def dict_flatten(d, separator='.'):
    ''' Credit: Flattening JSON objects in Python by Amir Ziai
        https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10'''

    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + separator)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + separator)
                i += 1
        else:
            out[name[:-1]] = x

    flatten(d)
    return out

class FilterModule(object):
    ''' Ansible filters. Interface to Python dictionary methods.

        5.5. Dictionaries
        https://docs.python.org/3/tutorial/datastructures.html#dictionaries'''

    def filters(self):
        return {
            'dict_add_hash' : dict_add_hash,
            'dict_del_key' : dict_del_key,
            'dict_keys' : dict_keys,
            'dict_merge' : dict_merge,
            'dict_sorted' : dict_sorted,
            'dict_search_key' : dict_search_key,
            'dict_prefix_keys' : dict_prefix_keys,
            'dict_flatten': dict_flatten
        }
