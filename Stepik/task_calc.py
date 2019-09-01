a = float(input())
b = float(input())
c = input()

if c == '+':
    print(a + b)
    
if c == '-':
    print(a - b)
    
if c == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
        
if c == '*':
    print(a * b)
    
if c == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)

if c == 'pow':
    print(a**b)
    
if c == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)