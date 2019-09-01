s=input()
n=len(s)
r=s[0]
c=1
for i in range(n):
    if n==1:
        r+=str(c)
    if i==0:
        continue
    if s[i-1] == s[i]:
        c+=1
    else:
        r+=str(c)+s[i]
        c=1
    if i==n-1:
        r+=str(c)
print(r)