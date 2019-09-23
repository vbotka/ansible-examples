# All rights reserved (c) 2019, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

from datetime import date, datetime

def datetime_epoch_strftime(epoch, format='%Y-%m-%d %H:%M:%S'):
    return datetime.fromtimestamp(float(epoch)).strftime(format)

class FilterModule(object):
    ''' Ansible filters. Interface to Python datetime methods.

        datetime Basic date and time types
        https://docs.python.org/3/library/datetime.html'''

    def filters(self):
        return {
            'datetime_epoch_strftime': datetime_epoch_strftime
        }
