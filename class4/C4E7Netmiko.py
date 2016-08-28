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

print "Changing the buffer size..."
time.sleep(2)
Pynet2ConfigCommands = ['logging buffer 6666']
Pynet2ConfigChange = Pynet2Connect.send_config_set(Pynet2ConfigCommands)
print "\n", Pynet2ConfigCommands, "\n\n"

print "Exiting configuration mode..."
time.sleep(2)
Pynet2ExitConfig = Pynet2Connect.exit_config_mode()
print "\n", Pynet2Prompt, "\n\n"

print "Checking if the command took effect..."
time.sleep(2)
Pynet2ConfigChangeCheck = Pynet2Connect.send_command('show run | i logging')
print "\n\n", Pynet2Prompt, "show run | i logging\n", Pynet2ConfigChangeCheck, "\n\n"


