import os.path
import re

from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.inventory.group import Group


PATH_PLACEHOLDER = 'IP_BASED_GROUPS'
IP_RE = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')


class InventoryModule(BaseInventoryPlugin):
    '''
    This inventory plugin does not create any hosts, but just adds groups based
    on IP addresses. For each host whose ansible_host looks like an IPv4
    address (e.g. 1.2.3.4), a corresponding group is created by prefixing the
    IP address with 'ip_' and replacing dots by underscores (e.g. ip_1_2_3_4).

    Use it by putting the literal string IP_BASED_GROUPS at the end of the list
    of inventory sources.
    '''

    NAME = 'ip_based_groups'

    def verify_file(self, path):
        return self._is_path_placeholder(path)

    def parse(self, inventory, loader, path, cache=True):
        if not self._is_path_placeholder(path):
            return
        for host_name, host in inventory.hosts.items():
            ansible_host = host.vars.get('ansible_host', '')
            if self._is_ip_address(ansible_host):
                group = 'ip_' + ansible_host.replace('.', '_')
                inventory.add_group(group)
                inventory.add_host(host_name, group)

    def _is_path_placeholder(self, path):
        return os.path.basename(path) == PATH_PLACEHOLDER

    def _is_ip_address(self, s):
        return bool(IP_RE.match(s))
