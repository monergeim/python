a = int(input())
b = int(input())
c = int(input())
ma=a
mi=a
su=a+b+c

if b>ma:
    ma=b
    
if c>ma:
    ma=c

if b<mi:
    mi=b
    
if c<mi:
    mi=c
print(ma)
print(mi)
print(su-mi-ma)