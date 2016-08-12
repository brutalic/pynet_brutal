#!/usr/bin/python

import getpass
import snmp_helper
from snmp_helper import snmp_get_oid,snmp_extract
import yaml


DeviceIp1 = '184.105.247.70'
DeviceIp2 = '184.105.247.71'
SnmpPort = 161
sysNameOID = '.1.3.6.1.2.1.1.5.0'
sysDescOID = '.1.3.6.1.2.1.1.1.0'

#Connecting to the devices, using methods from getpass library
DeviceIp1 = raw_input("pynet-rtr1 IP address: ")
DeviceIp2 = raw_input("pynet-rtr2 IP address: ")
SnmpString = getpass.getpass(prompt="Community string: ")

#Creating a tuple for each device, consisting of the IP, SNMP string and SNMP port
SnmpDevice1 = (DeviceIp1, SnmpString, SnmpPort)
SnmpDevice2 = (DeviceIp2, SnmpString, SnmpPort)

#Creating a loop to cycle through each device's information, using the snmp_helper lybrary methods
for SnmpDevices in (SnmpDevice1, SnmpDevice2):
    for OIDs in (sysNameOID, sysDescOID):
        SnmpInformation = snmp_get_oid(SnmpDevices, oid=OIDs)
        SnmpDescOutput = snmp_extract(SnmpInformation)
        
        #Printing results to a yaml file
        SmpFileOutput = 'SnmpInformation.txt'
        with open(SmpFileOutput, "a") as f:
            f.write(yaml.safe_dump(SnmpDescOutput, default_flow_style=False))
print "\nResults printed to a yaml file.\n"

