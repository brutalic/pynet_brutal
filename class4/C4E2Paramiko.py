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

print "\nYou logged in!"
ShellOutput = RemoteConn.recv(5000)
print ShellOutput
print "\n"


ShellOutput = RemoteConn.send("conf t\n")
print "\nEntering configuration mode..."
time.sleep(2)
ShellOutput = RemoteConn.recv(65535)
print ShellOutput


ShellOutput = RemoteConn.send("logging buffered 4444\n")
print "\nChanging the logging buffer to 4444..."
time.sleep(2)
ShellOutput = RemoteConn.recv(65535)
print ShellOutput


ShellOutput = RemoteConn.send("end\n")
print "\nExiting configuration mode..."
time.sleep(2)
ShellOutput = RemoteConn.recv(65535)
print ShellOutput


ShellOutput = RemoteConn.send("show run | i logging buff\n")
print "\nVerifying the logging buffered is changed..."
time.sleep(2)
ShellOutput = RemoteConn.recv(65535)
print ShellOutput


RemoteConn.close()
