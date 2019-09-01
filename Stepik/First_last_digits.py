a = int(input())
f1 = a // 100000 
f2 = a // 10000
f3 = a // 1000
l1 = a // 100
l2 = a // 10
l3 = a % 10
f = f1+f2+f3
l = l1+l2+l3

if f==l:
    print ('Счастливый')
else:
    print ('Обычный') 
