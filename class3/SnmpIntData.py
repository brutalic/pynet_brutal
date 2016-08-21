#!/usr/bin/python

import snmp_helper
import time
import yaml


DeviceIp1 = '184.105.247.70'
DeviceIp2 = '184.105.247.71'

SnmpUser = 'pysnmp'
SnmpAuth = 'galileo1'
SnmpEncr = 'galileo1'

snmp_user = (SnmpUser, SnmpAuth, SnmpEncr)
pynet_rtr1 = (DeviceIp1, 161)
pynet_rtr2 = (DeviceIp2, 161)


SnmpOids = (
            ('sysName', '1.3.6.1.2.1.1.5.0', None),
            ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
            ('Fa4 ifDescr', '1.3.6.1.2.1.2.2.1.2.5', None),
            ('Fa4 ifInOctets', '1.3.6.1.2.1.2.2.1.10.5', True),
            ('Fa4 ifInUcastPkts', '1.3.6.1.2.1.2.2.1.11.5', True),
            ('Fa4 ifOutOctets', '1.3.6.1.2.1.2.2.1.16.5', True),
            ('Fa4 ifOutUcastPkts', '1.3.6.1.2.1.2.2.1.17.5', True),
            )

TimeOut = time.time() + 65
StartTime = time.time()
time.sleep(1)

while True:
    #Checking to see if the time has ended. It is currently set to 65 seconds.
    if time.time() > TimeOut:
        break
    #Tracking the time that has passed, and printing it out as the while and for loop are going
    ElapsedTime = time.time() - StartTime
    print "%s %s" % (format('time', '>20'), format(ElapsedTime, '>2'))
    #For loop that reads all the SNMP data assigned above with a time sleep at the end of 5 seconds
    for Desc,Oid,Count in SnmpOids:
        SnmpData = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=Oid)
        SnmpOutput = snmp_helper.snmp_extract(SnmpData)
        print "%s %s" % (format(Desc, '>20'), format(SnmpOutput, '>2'))
    print "\n"
    time.sleep(5)

