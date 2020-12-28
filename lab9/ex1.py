def mulfunc(n):
  if n == 0:
    return 0
  else:
     return 3 + mulfunc(n-1)
print(mulfunc(5))