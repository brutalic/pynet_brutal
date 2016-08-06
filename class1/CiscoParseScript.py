#!/usr/bin/python

from ciscoconfparse import CiscoConfParse


cisco_config = CiscoConfParse("ciscohost.txt")
#print cisco_config

crypto_find = cisco_config.find_objects(r"^crypto map CRYPTO")
#print crypto_find

#listing all the entries that begin with crypto map CRYPTO and the PFS lines
print "\nDisplaying all the crypto maps that use PFS group and the indented config within each crypto map\n"
for entry in crypto_find:  
    print entry.text
    for child in entry.children:
        print child.text


#Listing all the Crypto entries that do not contain AES encryption
no_aes_find = cisco_config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")
print "\n\nDisplaying all entries that do not contain AES encryption\n"
for entry in no_aes_find:
    print entry.text
    for child in entry.children:
        print child.text
print "\n"
     

