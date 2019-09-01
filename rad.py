#!/usr/bin/env python
def radiationExposure(start, stop, step):
    def f(x):
        import math
        return 10*math.e**(math.log(0.5)/5.27 * x)
    res = 0
    n=start
    while n < stop:
        res = res + f(n)*step
        print f(n)
        print res
        n += step
    return res


print radiationExposure(0, 1, 0.25)