def sumfunc(alist,result = 0):
  for i in alist:
    if type(i) == list:
      sumfunc(i)
    else:
      result = result + i
  return result
res = sumfunc([3,12,76,[4,56,43],[2,8],81,75])
print(res)