#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass
import time

Pass = getpass()

Pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': Pass,
}

Pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': Pass,
    'port': 22,
}

JuniperSRX = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': Pass,
    'secret': '',
    'port': 22,
}


Pynet1Connect = ConnectHandler(**Pynet1)
Pynet2Connect = ConnectHandler(**Pynet2)
JuniperConnect = ConnectHandler(**JuniperSRX)

#To check out the dictionary options udner  the ConnectHandler, you could do the following below:
#Pynet1DIR = dir(Pynet1Connect)
#print Pynet1DIR
print "Logging in..."
time.sleep(1)
Pynet1Prompt = Pynet1Connect.find_prompt()
Pynet2Prompt = Pynet2Connect.find_prompt()
JuniperPrompt = JuniperConnect.find_prompt()
print "\n", Pynet1Prompt, "\n", Pynet2Prompt, "\n", JuniperPrompt, "\n\n"


print "Checking the arp tables...\n"
time.sleep(2)
Pynet1IpInt = Pynet1Connect.send_command('show arp')
Pynet2IpInt = Pynet2Connect.send_command('show arp')
JuniperIpInt = JuniperConnect.send_command('show arp')
print Pynet1Prompt, "show arp\n", Pynet1IpInt, "\n\n"
print Pynet2Prompt, "show arp\n", Pynet2IpInt, "\n\n"
print JuniperPrompt, "show arp\n", JuniperIpInt, "\n"


