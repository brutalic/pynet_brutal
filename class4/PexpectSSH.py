#!/usr/bin/env/python

import pexpect
import sys
from getpass import getpass
import time
import re


def main():
    DeviceIp = '184.105.247.76'
    User = 'pyclass'
    Port = 22
    Pass = getpass()

    SSHconn = pexpect.spawn('ssh -l {} {} -p {}'.format(User, DeviceIp, Port))
    SSHconn.timeout = 3
    SSHconn.expect('assword:')
    SSHconn.sendline(Pass)
    SSHconn.expect('>')

    SSHconn.sendline('set cli screen-length 10000')
    SSHconn.expect('>')
    print SSHconn.before,SSHconn.after
    time.sleep(1)

    SSHconn.sendline('show configuration | display set')
    SSHconn.expect('>')
    print SSHconn.before,SSHconn.after
    time.sleep(1)

    #You can define the timeout what to display if it times out
    try:
        SSHconn.sendline('show version')
        #A bogus expectation was given below
        SSHconn.expect('blah-blah')
        print SSHconn.before,SSHconn.after
    except pexpect.TIMEOUT:
        print "No results were found for your given request!\n"

    #You can do special matching using the "re" library. The example below:
    #r - stands for "raw strings"
    #^Model - any string that starts with JUN
    #.*] - any sequence of 0 or more characters ending with ]
    #.*$ - any sequence of 0 or more characters end of the line
    Pattern = re.compile(r'^Model.*$', re.MULTILINE)
    SSHconn.sendline('show version')
    SSHconn.expect(Pattern)
    print SSHconn.before,SSHconn.after

if __name__ == "__main__":
    main()
