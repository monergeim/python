Short Description:
This is interactive metrics script which use psutil - cross-platform library for retrieving information on running processes and system utilization.

Full Description:
#Where to get help:
https://github.com/monergeim/metrics/wiki, https://pypi.org/help/, https://www.python.org/about/help/ or Stack Overflow

#Where to file issues:
https://github.com/monergeim/metrics/issues

#Maintained by:
Git repository owner

#Supported architectures:
amd64, arm32v5, arm32v6, arm32v7, arm64v8, i386, ppc64le, s390x, windows-amd64

#What is metrics script?
Based on python and psutil open library
From python perspective used 2 packages: psutil and argparse

#How to use this script:
mon.py [-h] arg

positional arguments:
  arg         enter argument mem or cpu to see details

optional arguments:
  -h, --help  show this help message and exit
  
The script require mandatory single parameter to specify which metrics set to print:
* cpu - prints CPU metrics
* mem - prints RAM metrics

#License:
GPL

#Docker image:
https://hub.docker.com/r/monergeim/metrics/
