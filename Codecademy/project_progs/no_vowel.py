def anti_vowel(text):
  out=''
  for l in text:
    if l not in "aeiouAEIOU":
      out+=l
  return out
