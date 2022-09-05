def examples_tags(l):

    tags = [{'ex': l[0], 'tag': t.strip()} for t in l[1][1:-1].split(';')[1:-1]]
    group = l[1][1:-1].split(';')[0]
    return {'group': group, 'tags': tags}


class FilterModule(object):
    ''' Ansible filter'''

    def filters(self):
        return {
            'examples_tags': examples_tags,
        }
