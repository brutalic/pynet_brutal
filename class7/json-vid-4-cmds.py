#!/usr/bin/python

import jsonrpclib
import time
import ssl
from pprint import pprint

ssl._create_default_https_context = ssl._create_unverified_context
ip = '184.105.247.72'
port = '443'


username = 'admin1'
password = '99saturday'


switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip, port)
switch_url = switch_url + '/command-api'


remote_connect = jsonrpclib.Server(switch_url)
print remote_connect

commands = []
commands.insert (0, 'configure terminal')
commands.insert (0, {'cmd': 'enable', 'input': ''})
commands.append('vlan 222')
commands.append('name green')

print commands

CommandsResponse = remote_connect.runCmds(1, commands)
pprint(CommandsResponse)

