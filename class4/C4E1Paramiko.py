#!/usr/bin/python

import paramiko
import getpass
from getpass import getpass
import time


DeviceIp = '184.105.247.71'
User = 'pyclass'
Pass = getpass()
Port = 22

RemoteConnPre = paramiko.SSHClient()
RemoteConnPre.load_system_host_keys()
RemoteConnPre.connect(DeviceIp, username=User, password=Pass, look_for_keys=False, allow_agent=False, port=Port)
RemoteConn = RemoteConnPre.invoke_shell()

RemoteConn.settimeout(3.3)

ShellOutput = RemoteConn.send("term length 0\n")
print "\nSetting the terminal length to 0..."
time.sleep(2)
ShellOutput = RemoteConn.recv(65535)
print ShellOutput


ShellOutput = RemoteConn.send("show version\n")
time.sleep(1)
AnythingToBeRead = RemoteConn.recv_ready()
print "\nIs there any data to be read?"
print AnythingToBeRead
time.sleep(1)
ShellOutput = RemoteConn.recv(65535)
print "Displaying the device's version output..."
time.sleep(2)
print ShellOutput

RemoteConn.close()
