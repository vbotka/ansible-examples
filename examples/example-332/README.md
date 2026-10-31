# ansible.netcommon.parse_cli_textfsm

Parse boot configuration from a Cisco switch:

```console
---------------------------
Switch 1
---------------------------
Current Boot Variables:
BOOT variable = flash:packages_01.conf;

Boot Variables on next reload:
BOOT variable = flash:packages_02.conf;
Manual Boot = no
---------------------------
Switch 2
---------------------------
Current Boot Variables:
BOOT variable = flash:packages_A.conf;

Boot Variables on next reload:
BOOT variable = flash:packages_B.conf;
Manual Boot = yes
Enable Break = no
```

```yaml
PLAY [Parse boot variables] ****************************************************

TASK [ansible.utils.cli_parse] *************************************************
ok: [localhost]

TASK [ansible.builtin.debug] ***************************************************
ok: [localhost] => 
    parsed_records.parsed:
    -   CURRENT_BOOT: flash:packages_01.conf;
        ENABLE_BREAK: ''
        MANUAL_BOOT: 'no'
        NEXT_BOOT: flash:packages_02.conf;
        SWITCH_ID: '1'
    -   CURRENT_BOOT: flash:packages_A.conf;
        ENABLE_BREAK: 'no'
        MANUAL_BOOT: 'yes'
        NEXT_BOOT: flash:packages_B.conf;
        SWITCH_ID: '2'

TASK [ansible.builtin.debug] ***************************************************
ok: [localhost] => 
    parsed_records.parsed | to_boot_dict:
        '1':
            current_boot:
                config: flash:packages_01.conf
            id: '1'
            next_boot:
                config: flash:packages_02.conf
                manual_boot: false
        '2':
            current_boot:
                config: flash:packages_A.conf
            id: '2'
            next_boot:
                config: flash:packages_B.conf
                enable_break: false
                manual_boot: true

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
