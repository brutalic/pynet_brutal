#!/usr/bin/python

import paramiko
import getpass
from getpass import getpass
import time


DeviceIp = '184.105.247.70'
User = 'pyclass'
Pass = getpass()
Port = 22

RemoteConnPre = paramiko.SSHClient()
RemoteConnPre.load_system_host_keys()
RemoteConnPre.connect(DeviceIp, username=User, password=Pass, look_for_keys=False, allow_agent=False, port=Port)
RemoteConn = RemoteConnPre.invoke_shell()

RemoteConn.settimeout(6.0)

ShellOutput = RemoteConn.send("show ip int brief\n")
time.sleep(2)
AnythingToBeRead = RemoteConn.recv_ready()
print "\nIs there any data to be read?"
print AnythingToBeRead
ShellOutput = RemoteConn.recv(65535)

time.sleep(1)
print ShellOutput

#Testing additional command (multiple commands test)
ShellOutput = RemoteConn.send("show int desc\n")
time.sleep(2)
AnythingToBeRead = RemoteConn.recv_ready()
print "\nIs there any data to be read?"
print AnythingToBeRead
ShellOutput = RemoteConn.recv(65535)

time.sleep(1)
print ShellOutput

#If there is data larger than 65535 to be read (for example "show run" commandi), then
#it can be executed in a while loop reading the channel, and each time it's read, you check
#if there is more data gathered using the "recv_ready()" function, and you read the rest
#and check it each time. Also do sleep time in between


