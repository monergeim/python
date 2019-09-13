#!/usr/bin/env python

# mpg to fuel outcome per 100 km calculator

import sys
tank = 18.6
mpg = int(sys.argv[1])
mile = 1.609344
gal = 3.78541
res = 100/(mpg * (mile/gal))
dist = mpg*tank*mile

print str(res) + " liters per 100 km"
print "With tank size " + str(tank) + " gallons you can can drive without refuel " + str(dist) + " km"
