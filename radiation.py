#!/usr/bin/env python
def radiationExposure(start, stop, step):
    def f(x):
        import math
        return 10*math.e**(math.log(0.5)/5.27 * x)
    if start == stop:
        return 0
    return f(start)*step+radiationExposure(start + step, stop, step)  


print radiationExposure(600, 1200, 5)