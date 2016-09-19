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

time.sleep(1)

response = remote_connect.runCmds(1, ['show version'])
pprint(response)

response2 = remote_connect.runCmds(1, ['show arp'])
print '\n'
pprint(response2)
#Peel the response2 like an onion
print type(response2)
print len(response2)

dictionary = response2[0]
print dictionary.keys()

ipv4 = dictionary['ipV4Neighbors']
print '\n'
print ipv4
print len(ipv4)

print '\n'
pprint(ipv4[0])
