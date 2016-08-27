#!/usr/bin/env/python

import pexpect
import sys
from getpass import getpass
import time
import re


def main():
    DeviceIp = '184.105.247.71'
    User = 'pyclass'
    Port = 22
    Pass = getpass()

    SSHconn = pexpect.spawn('ssh -l {} {} -p {}'.format(User, DeviceIp, Port))
    SSHconn.timeout = 5
    SSHconn.expect('assword:')
    SSHconn.sendline(Pass)
    SSHconn.expect('#')
    print SSHconn.before,SSHconn.after
    
    try:
        SSHconn.sendline('show ip int br')
        SSHconn.expect('#')
        print SSHconn.before,SSHconn.after
        time.sleep(1)
    except pexpect.TIMEOUT:
        print "No results were found for your given request!\n"

if __name__ == "__main__":
    main()
