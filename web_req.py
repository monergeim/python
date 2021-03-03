#!/usr/bin/python3

import sys
import os
import requests
from subprocess import call

w_link = sys.argv[1]
x = requests.get(w_link)
line = 7257
message = "website has changes"
path = "/home/sergiilypnytskyi/git/python"
os.chdir(path)

with open("Output_new.txt", "w") as text_file:
    print(x.text, file=text_file)

with open('Output.txt') as f1, open('Output_new.txt') as f2:
    l1=f1.readlines()
    l2=f2.readlines()
#    print(l1[line])
#    print(l2[line])
    if l1[line] != l2[line]:
        print('Fail')
        call(["/usr/local/bin/telegram-send", message])
        with open("Output.txt", "w") as text_file:
            print(x.text, file=text_file)



#in cron task could be like: 30 11 * * * user ~/git/python/web_req.py https://sturm.com.ua/helikon-tex.html
