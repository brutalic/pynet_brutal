#!/usr/bin/python

import snmp_helper
#from snmp_helper import snmp_get_oid_v3
#from snmp_helper import snmp_extract

DeviceIp = '184.105.247.70'

SnmpUser = 'pysnmp'
SnmpAuth = 'galileo1'
SnmpEncr = 'galileo1'

snmp_user = (SnmpUser, SnmpAuth, SnmpEncr)
pynet_rtr1 = (DeviceIp, 161)
pynet_rtr2 = (DeviceIp, 161)

SnmpData = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='.1.3.6.1.2.1.1.5.0')
output = snmp_helper.snmp_extract(SnmpData)

print SnmpData
print output
