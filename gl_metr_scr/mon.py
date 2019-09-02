#!/usr/bin/env python

import psutil
import argparse

#Parse arguments
myparser = argparse.ArgumentParser()
myparser.add_argument("arg", help="enter argument mem or cpu to see details")
myargs = myparser.parse_args()

#Metric condition
if myargs.arg == "mem":
  res_virt = psutil.virtual_memory()
  res_swap = psutil.swap_memory()
  print ("virtual total", res_virt[0]);
  print ("virtual used", res_virt[3]);
  print ("virtual free", res_virt[4]);
  print ("virtual shared", res_virt[9]);
  print ("swap total", res_swap[0]);
  print ("swap used", res_swap[1]);
  print ("swap free", res_swap[2]);

elif myargs.arg == "cpu":
  result = psutil.cpu_times_percent(interval=1)
  print ("system.cpu.idle", result[3]);
  print ("system.cpu.user", result[0]);
  print ("system.cpu.guest", result[8]);
  print ("system.cpu.iowait", result[4]);
  print ("system.cpu.stolen", result[7]);
  print ("system.cpu.system", result[2]);

else:
  print ("Incorrect argument, please use -h for help")

