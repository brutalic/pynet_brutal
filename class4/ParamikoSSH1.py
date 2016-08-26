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
RemoteConnPre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

RemoteConnPre.connect(DeviceIp, username=User, password=Pass, look_for_keys=False, allow_agent=False, port=Port)

RemoteConn = RemoteConnPre.invoke_shell()

ShellOutput = RemoteConn.recv(10000)
print ShellOutput

RemoteConn.send("show ip int br\n")
time.sleep(2)
ShellOutput = RemoteConn.recv(10000)
print ShellOutput
