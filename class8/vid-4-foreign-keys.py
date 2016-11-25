#!/usr/bin/env/python

import django
django.setup()

from net_system.models import NetworkDevice, Credentials

devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

#print devices
#print creds


std_creds = creds[0]
arista_creds = creds[1]

my_device = NetworkDevice.objects.get(device_name='pynet-rtr1')

print my_device

my_creds = my_device.credentials
print my_creds

my_device.vendor = 'cisco'
my_device.model = '881'
my_device.save()

print devices

#pynet_rtr2 = devices[1]
#print pynet_rtr2
#pynet_rtr2_delete = pynet_rtr2.delete()

print "\nAfter deletion..."
print devices, "\n\n"

devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

print devices, creds

pynet_rtr2 = devices[3]
print pynet_rtr2

std_creds = creds[0]
pynet_rtr2.credentials = std_creds
pynet_rtr2.save()

print devices, pynet_rtr2.credentials
