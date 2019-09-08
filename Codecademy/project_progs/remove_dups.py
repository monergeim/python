ef remove_duplicates(lst):
  out=[]
  for n1 in lst:
    if n1 not in out:
      out.append(n1)
  return out
