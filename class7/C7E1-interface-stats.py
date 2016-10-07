#!/usr/bin/python

import pyeapi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

pynet_sw3 = pyeapi.connect_to("pynet-sw3")

print pynet_sw3

sw3_int_stats = pynet_sw3.enable("show interfaces")
sw3_int_stats = sw3_int_stats[0]['result']
sw3_int_stats = sw3_int_stats['interfaces']
#pprint(sw3_int_stats)

main_statistics = {}
for sw3_interface, sw3_int_counters_stat in sw3_int_stats.items():
    sw3_int_counters = sw3_int_counters_stat.get('interfaceCounters', {})
    main_statistics[sw3_interface] = (sw3_int_counters.get('inOctets'), sw3_int_counters.get('outOctets'))
#   print main_statistics

print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets") 
for intf, octets in main_statistics.items(): 
    print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1]) 

