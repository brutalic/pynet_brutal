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
    'port': 22,
}

Pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': Pass,
    'port': 22,
}

Pynet1Connect = ConnectHandler(**Pynet1)
Pynet2Connect = ConnectHandler(**Pynet2)

print "Logging in..."
time.sleep(1)
Pynet1Prompt = Pynet1Connect.find_prompt()
Pynet2Prompt = Pynet2Connect.find_prompt()
print "\n", Pynet1Prompt, "\n", Pynet2Prompt, "\n\n"

print "Entering configuration mode..."
time.sleep(2)
Pynet1Config = Pynet1Connect.config_mode()
Pynet2Config = Pynet2Connect.config_mode()
print "\n", Pynet1Config, "\n", Pynet2Config, "\n\n"

print "Changing the buffer size and the console logging access..."
time.sleep(2)
CiscoConfigCommands = ['logging buffer 8888',
                        'no logging console']
Pynet1ConfigChange = Pynet1Connect.send_config_set(CiscoConfigCommands)
Pynet2ConfigChange = Pynet2Connect.send_config_set(CiscoConfigCommands)
time.sleep(1)
print "\n", Pynet1ConfigChange, "\n", Pynet2ConfigChange, "\n\n"

print "Checking if devices are still in configuration mode...\n"
time.sleep(1)
Pynet1ConfigCheck = Pynet1Connect.check_config_mode()
Pynet2ConfigCheck = Pynet2Connect.check_config_mode()
print "Is", Pynet1Prompt, "in config mode?", Pynet1ConfigCheck
time.sleep(1)
print "Is", Pynet2Prompt, "in config mode?", Pynet2ConfigCheck, "\n\n"
time.sleep(1)

print "Checking if the commands took effect..."
time.sleep(2)
Pynet1ConfigChangeCheck = Pynet1Connect.send_command('show run | i logging')
Pynet2ConfigChangeCheck = Pynet2Connect.send_command('show run | i logging')
print "\n", Pynet1Prompt, "show run | i logging\n", Pynet1ConfigChangeCheck, "\n", Pynet2Prompt, "show run | i logging\n", Pynet2ConfigChangeCheck, "\n\n"

