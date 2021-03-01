#!/usr/bin/python3

import sys
import requests

w_link = sys.argv[1]
x = requests.get(w_link)


#print(x.text)

with open('Output_new.txt', 'w') as file:
    file.write(x.text)
    file.close()

with open('Output.txt') as f1, open('Output_new.txt') as f2:
    for line1, line2 in zip(f1, f2):
        if line1 != line2:
            print("Fail")
            print(line1)
            print(line2)