print("World.\nHold on. Ta-ta-ta-tata")

a=35
b="Hi"
name="mr.serg li"

print(str(a) + "\n" + b)
print(name.upper())
print(b.lower())
print(name.title())
x=0

for i in range(0,4):
    x+=1
    if i==2:
        continue
    print(i)
    print("x="+str(x))

msg="dlrow olleh"

print (f"Hello, {name.title()}. You are {a}.")
print (f"Hello dlrow")
print(msg[::-1])