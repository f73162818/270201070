def reversefunc(l):
  if len(l) == 0:
    return []
  else:
    reverselist = l[-1]
    l = l[:-1]
    return reverselist.append(reversefunc(l))
reversed = reversefunc ([1, 2, 3, 4])
print(reversed)

