#!/usr/bin/env/python

import pyeapi 
import argparse 
#from eapi_vlan import check_vlan_exists, configure_vlan 
#from ansible.module_utils.basic import *

#The script does not function properly. Refer to the script written by Kirk B.

eapi_conn = pyeapi.connect_to("pynet-sw3")

#Parsing arguments
parser = argparse.ArgumentParser(description="Adding/removing VLANs")
parser.add_argument("vlan_id", action="store", type=int) 
parser.add_argument( 
    "--name", 
    action="store",
    dest="vlan_name", 
    type=str 
) 
parser.add_argument("--remove", action="store_true") 
 
cli_args = parser.parse_args() 
vlan_id = cli_args.vlan_id 
remove = cli_args.remove 
vlan_name = cli_args.vlan_name 


#Check to see if the Vlan exists
#check_vlan = check_vlan(eapi_conn, vlan_id)
vlan_id = str(vlan_id)
cmd = 'show vlan id {}'.format(vlan_id)
try:
    response = eapi_conn.enable(cmd)
    check_vlan = pyeapi_result(response)['vlans']
#    return check_vlan[vlan_id]['name']
except (pyeapi.eapilib.CommandError, KeyError):
    pass
check_vlan = check_vlan(eapi_conn, vlan_id)
#return False


#Name the vlan
vlan_name=None
command_str1 = 'vlan {}'.format(vlan_id)
cmd = [command_str1]
if vlan_name is not None:
    command_str2 = 'name {}'.format(vlan_name)
    cmd.append(command_str2)

#Check if VLAN exists
#check_vlan = check_vlan_exists(eapi_conn, vlan_id)

#Check if action is remove or add 
if remove: 
    if check_vlan: 
        print "VLAN exists, removing it" 
        command_str = 'no vlan {}'.format(vlan_id) 
        eapi_conn.config([command_str]) 
    else: 
        print "VLAN does not exist, no action required" 
else: 
    if check_vlan: 
        if vlan_name is not None and check_vlan != vlan_name: 
            print "VLAN already exists, setting VLAN name" 
            configure_vlan(eapi_conn, vlan_id, vlan_name) 
        else: 
            print "VLAN already exists, no action required" 
    else: 
        print "Adding VLAN including vlan_name (if present)" 
        configure_vlan(eapi_conn, vlan_id, vlan_name) 


