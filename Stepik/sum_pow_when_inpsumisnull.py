s=0
spow=0
while True:
  i=int(input())
  spow+=i**2
  s+=i
  if s==0:
    break
print(spow)