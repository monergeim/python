a = int(input())
b = int(input())
c = int(input())
d = int(input())

print "\t",
i = c
while i <= d:
    if i == d:
      print str(i)
    else:
      print str(i) + "\t",
    i += 1
for i in range(a, b + 1):
    print str(i) + "\t",
    for j in range(c, d + 1):
        if j != d:
            print str(j*i) + "\t",
        else:
            print (j*i)