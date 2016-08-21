#!/usr/bin/python

import pygal

Fa4_in_octets = [103875936, 103879432, 103879432, 103887814, 103892535, 103892535, 103899662, 103903053, 103903053, 103909788, 103909788]
Fa4_out_octets = [238828964, 238833172, 238842430, 238842430, 238847017, 238847017, 238854380, 238857993, 238857993, 238865398, 238871834]

Fa4_in_packets = [790093, 790114, 790114, 790170, 790197, 790197, 790239, 790261, 790261, 790304, 790304]
Fa4_out_packets = [784310, 784331, 784394, 784394, 784421, 784421, 784463, 784485, 784485, 784528, 784564]

LineChart = pygal.Line()

LineChart.title = "Input/Output Packets and Bytes"
LineChart.x_labels = ['1.00111699104', '7.22944092751', '13.4874489307', '19.7507779598', '25.9744579792', '32.2459490299', '38.5079898834', '44.760794878', '51.0133090019', '57.2490930557', '63.5316929817']
LineChart.add('InPackets', Fa4_in_packets)
LineChart.add('OutPackets', Fa4_in_packets)
LineChart.add('InBytes', Fa4_in_octets)
LineChart.add('OutBytes', Fa4_in_octets)

LineChart.render_to_file('linechart.svg')
