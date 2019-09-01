a = int(input())
b = int(input())
ma = b
mi = a
if a >= b:
    ma = a
    mi = b
if ma % a == 0 and ma % b == 0:
    print(ma)
else:
    d = mi
    while d % a != 0 or d % b != 0:
        d += mi
    print(d)