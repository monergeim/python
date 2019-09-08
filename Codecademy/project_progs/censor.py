def censor(text,word):
  out=[]
  s='*' * len(word)
  for w in text.split():
    if w == word:
      out.append(s)
    else:
      out.append(w)
  return " ".join(out)
