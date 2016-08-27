#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass
import time

Pass = getpass()


Pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': Pass,
    'port': 22,
}


Pynet2Connect = ConnectHandler(**Pynet2)

print "Logging in..."
time.sleep(1)
Pynet2Prompt = Pynet2Connect.find_prompt()
print "\n", Pynet2Prompt, "\n\n"

print "Entering configuration mode..."
time.sleep(2)
Pynet2Config = Pynet2Connect.config_mode()
print "\n", Pynet2Config, "\n\n"

print "Checking if the router is in configuration mode..."
time.sleep(1)
print Pynet2Connect.check_config_mode()
