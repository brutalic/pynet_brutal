#!/usr/bin/python

import pyeapi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#ip = '184.105.247.72'
#port = '443'

#username = 'admin1'
#password = '99saturday'

#pynet_sw3 = pyeapi.connect_to("pynet_sw3")
pynet_sw4 = pyeapi.connect_to("pynet_sw4")

#print pynet_sw3
#print pynet_sw4

