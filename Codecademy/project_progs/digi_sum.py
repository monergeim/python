def digit_sum(n):
  w = 1
  s = 0
  while n!=0:
    s+=n%10
    n=n//10
  return s
