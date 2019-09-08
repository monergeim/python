def reverse(text):
  txet=''
  i = len(text) - 1
  while i>=0:
    txet+= text[i]
    i-=1
  return txet
