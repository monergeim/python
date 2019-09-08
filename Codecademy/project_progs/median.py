def median(lst):
  l = sorted(lst)
  le=len(lst)
  if le%2 == 0:
    out=(l[(le//2-1)]+l[(le//2)])/2.0
  else:
    out=l[(le//2)]
  return out
