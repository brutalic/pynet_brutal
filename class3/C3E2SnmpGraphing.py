#!/usr/bin/python

import pygal

Fa4_in_octets = [106040793, 106050195, 106060118, 106100549, 106118017, 106126519, 106153212, 106175845, 106187843, 106208760, 106219103, 106229225, 106238068]
Fa4_out_octets = [241802147, 241814878, 241826687, 241869533, 241889400, 241900815, 241928550, 241953232, 241968266, 241990677, 242003278, 242015114, 242026935]

Fa4_in_packets = [800532, 800577, 800619, 800902, 800994, 801030, 801231, 801376, 801435, 801567, 801613, 801658, 801696]
Fa4_out_packets = [795153, 795196, 795236, 795494, 795584, 795618, 795789, 795917, 795974, 796088, 796132, 796175, 796210]

LineChartBytes = pygal.Line()
LineChartBytes.title = "Input & Output Bytes"
LineChartBytes.x_labels = [1.00, 302.15, 603.31, 904.45, 1205.80, 1506.99, 1808.15, 2109.30, 2410.49, 2711.64, 3012.83, 3313.94, 3615.06]
LineChartBytes.add('InBytes', Fa4_in_octets)
LineChartBytes.add('OutBytes', Fa4_out_octets)
LineChartBytes.render_to_file('C3E2_input-output-octets.svg')

LineChartPackets = pygal.Line()
LineChartPackets.title = "Input & Output Packets"
LineChartPackets.x_labels = [1.00, 302.15, 603.31, 904.45, 1205.80, 1506.99, 1808.15, 2109.30, 2410.49, 2711.64, 3012.83, 3313.94, 3615.06]
LineChartPackets.add('InPackets', Fa4_in_packets)
LineChartPackets.add('OutPackets', Fa4_out_packets)
LineChartPackets.render_to_file('C3E2_input-output-unicast-packets.svg')

