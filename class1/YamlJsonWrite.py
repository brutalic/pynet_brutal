#!/usr/bin/python

import yaml
import json


mylist = ['dude', 'pizza', {'guitar': 'noise', 'drums': 'beat', 'bass': 'funk'}]

#Writting files to YAML
print "\nPrinting the list that will be written to a yaml file"
print yaml.dump(mylist)

yaml_output = 'yamloutput.yml'
with open(yaml_output, "w") as f:
    f.write(yaml.dump(mylist, default_flow_style=False))

#Writting files to JSON
print "\nPrinting the list that will be written to a json file"
print json.dumps(mylist)

json_output = 'jsonoutput.json'
with open(json_output, "w") as f:
    json.dump(mylist, f)
print "\n"

