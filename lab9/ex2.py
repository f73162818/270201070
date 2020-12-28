def hailstone(n,thelist=[]):
  thelist.append(int(n))
  if n == 1:
    strlist = ",".join(thelist)
    return strlist
  elif n%2 == 0:
    hailstone(n/2)
  elif n%2 == 1:
    hailstone(3*n+1)
