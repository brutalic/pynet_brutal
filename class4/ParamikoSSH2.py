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

ShellOutput = RemoteConn.recv(5000)
print ShellOutput

#time.sleep(2)

#Not sure how to execute multiple commands, but I suppose that would come in Paramiko video part 3
#The code below is not necessary correct
StandardIn, StandardOut,StandardErr = ShellOutput.exec_command('show ip int brief\n')
print StandardOut.read()

StandardIn, StandardOut,StandardErr = RemoteConnPre.exec_command('show int desc\n')
print StandardOut.read()


