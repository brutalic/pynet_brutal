#!/usr/bin/python

import pyeapi
import ssl
from pprint import pprint


ssl._create_default_https_context = ssl._create_unverified_context

#ip = '184.105.247.72'
#port = '443'

#username = 'admin1'
#password = '99saturday'

pynet_sw3 = pyeapi.connect_to("pynet-sw3")
pynet_sw4 = pyeapi.connect_to("pynet-sw4")

print pynet_sw3
print pynet_sw4

#print pyeapi.config_for('pynet-sw3')

config3 = pynet_sw3.get_config()
for line in config3:
    print line

sw3_version = pynet_sw3.enable("show version")
pprint(sw3_version)

sw3_arp = pynet_sw3.enable("show arp")
pprint(sw3_arp)

vlan_commands = ['vlan 333', 'name dude', 'vlan 444', 'name dudesky']
sw4_vlan = pynet_sw4.config(vlan_commands)

print sw4_vlan

config4 = pynet_sw4.get_config()
for line in config4:
    print line
