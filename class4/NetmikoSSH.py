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
print "\n", Pynet1Prompt, "\n", Pynet2Prompt, "\n", JuniperPrompt, "\n"


print "Entering configuration mode..."
time.sleep(2)
Pynet1Config = Pynet1Connect.config_mode()
Pynet2Config = Pynet2Connect.config_mode()
JuniperConfig = JuniperConnect.config_mode()
print "\n", Pynet1Config, "\n", Pynet2Config, "\n", JuniperConfig, "\n"

#Instead of printing out the config mode string, you can call the function "check_config_mode()"
#Pynet1Connect.check_config_mode()

print "Exiting configuration mode..."
time.sleep(2)
Pynet1ExitConfig = Pynet1Connect.exit_config_mode()
Pynet2ExitConfig = Pynet2Connect.exit_config_mode()
JuniperExitConfig = JuniperConnect.exit_config_mode()
print "\n", Pynet1ExitConfig, "\n", Pynet2ExitConfig, "\n", JuniperExitConfig, "\n"


print "Checking interfaces' IPs..."
time.sleep(2)
Pynet1IpInt = Pynet1Connect.send_command('show ip int brief')
Pynet2IpInt = Pynet2Connect.send_command('show ip int brief')
JuniperIpInt = JuniperConnect.send_command('show interfaces terse | match "up    up"')
print "\n", Pynet1IpInt, "\n\n", Pynet2IpInt, "\n\n", JuniperIpInt, "\n"


print "Sending a few config commands to the Juniper..."
time.sleep(2)
JuniperConfig = JuniperConnect.config_mode()
JuniperConfigCommands = ['set interfaces vlan unit 0 description "Management Vlan 0"',
                            'set system host-name pynet-juniper-srx1']
JuniperConfigChange = JuniperConnect.send_config_set(JuniperConfigCommands)

JuniperConfigCheckCommand = ['show | compare']
JuniperConfigChangeCheck = JuniperConnect.send_config_set(JuniperConfigCheckCommand)
print "Displaying the change below...\n"
print JuniperConfigChangeCheck
time.sleep(1)

print "\nCommiting the change..."
JuniperConnect.commit()

time.sleep(60)
