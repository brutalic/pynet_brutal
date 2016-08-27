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
    print "\n"
    
    try:
        SSHconn.sendline('conf t')
        print "Entering configuration mode..."
        time.sleep(2)
        SSHconn.expect('#')
        print SSHconn.before,SSHconn.after
        print "\n"
        time.sleep(2)

        SSHconn.sendline('logging buffered 5555')
        print "Changing the logging buffer to 5555..."
        time.sleep(2)
        SSHconn.expect('#')
        print SSHconn.before,SSHconn.after
        print "\n"
        time.sleep(2)

        SSHconn.sendline('end')
        print "Exiting configuration mode..."
        time.sleep(2)
        SSHconn.expect('#')
        print SSHconn.before,SSHconn.after
        print "\n"
        time.sleep(2)

        SSHconn.sendline('show run | i logging buff')
        print "Verifying that the buffer is changed..."
        time.sleep(2)
        SSHconn.expect('#')
        print SSHconn.before,SSHconn.after
        print "\n"

    except pexpect.TIMEOUT:
        print "No results were found for your given request!\n"

if __name__ == "__main__":
    main()
