#!/bin/bash
sed -i_bkp '/(ADDRESS = (PROTOCOL = TCP)(HOST = 10.0.0.1)(PORT = 1501))/d;s/(ADDRESS = (PROTOCOL = TCP)(HOST = 10.0.0.2)(PORT = 1501))/(ADDRESS = (PROTOCOL = TCP)(HOST = my-site.com)(PORT = 1501))/;/(BALANCE = yes))/d' myconffile
