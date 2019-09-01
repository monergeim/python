a = int(input())
b = a % 10
c = a % 100

if 11 <= c <= 14 or b == 0 or 5<= b <= 9:
    print (str(a) + ' программистов') 
else:
    if b == 1:
        print (str(a) + ' программист')
    else:
        print (str(a) + ' программиста')