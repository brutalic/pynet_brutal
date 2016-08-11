#!/usr/bin/python

import telnetlib
import time
import yaml


IpDevice = '184.105.247.70'
TelnetPort = 23
TelnetTimeout = 5
User = 'pyclass'
Pass = '88newclass'

#Initiating a Telnet session
RemoteTelnet = telnetlib.Telnet(IpDevice, TelnetPort, TelnetTimeout)

#Login portion
TelnetUser = RemoteTelnet.read_until("sername: ", TelnetTimeout)
print TelnetUser
RemoteTelnet.write(User + "\n")

TelnetPass = RemoteTelnet.read_until("assword: ", TelnetTimeout)
print TelnetPass
RemoteTelnet.write(Pass + "\n")
time.sleep(1)
RemoteTelnet.read_very_eager()

#Adjusting the terminal length to zero
RemoteTelnet.write("term length 0" + "\n")
time.sleep(1)
RemoteTelnet.read_very_eager()


#Executing and displaying "show ip interface brief" command
RemoteTelnet.write("show ip interface brief" + "\n")
time.sleep(1)
ShowIpOutput = RemoteTelnet.read_very_eager()
print ShowIpOutput

RemoteTelnet.close()


print "\nPrinting output to a yaml file..."
yaml_output = 'ShowIp.yml'
with open(yaml_output, "w") as f:
    f.write(yaml.dump(ShowIpOutput, default_flow_style=False))
time.sleep(1)
print "\nDone!\n"


