#!/usr/bin/python3

import sys
import requests

w_link = sys.argv[1]
x = requests.get(w_link)

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
#print ("This is the name of the script: ", sys.argv[0])
#print ("This is the first arg: ", sys.argv[1])

print(x.text)
