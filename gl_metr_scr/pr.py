#!/usr/bin/env python

import argparse

#Parse arguments
myparser = argparse.ArgumentParser()
myparser.add_argument("arg", help="enter argument mem or cpu to see details")
myargs = myparser.parse_args()

#Metric condition
if myargs.arg == "mem":
  print ("mem")

elif myargs.arg == "cpu":
  print ("cpu")

else:
  print ("Incorrect argument, please use -h for help")

