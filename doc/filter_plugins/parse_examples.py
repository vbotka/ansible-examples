def examples_tags(lst):

    tags = [{'ex': lst[0], 'tag': t.strip()} for t in lst[1][1:-1].split(';')[1:-1]]
    group = lst[1][1:-1].split(';')[0]
    return {'group': group, 'tags': tags}


class FilterModule(object):
    ''' Ansible filter'''

    def filters(self):
        return {
            'examples_tags': examples_tags,
        }
