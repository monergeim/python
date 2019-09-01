fig = input()

if fig == 'круг':
    r = float(input())
    p = 3.14
    print(p*r**2)

if fig == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)

if fig == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a*b)
