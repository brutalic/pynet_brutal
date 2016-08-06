#!/usr/bin/python

import yaml
import json


#Reading from YAML file
print "\n***Printing from the YAML file***" 
yamlfile = 'yamloutput.yml'
with open (yamlfile) as f:
    yamllist = yaml.load(f)
print yamllist
print "\n"

#Reading from JSON file
print "\n***Printing from the JSON file***"
jsonfile = 'jsonoutput.json'
with open (jsonfile) as f:
    jsonlist = json.load(f)
print jsonlist
print "\n"


