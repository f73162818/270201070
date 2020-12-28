def harmonicsum(n):
  if n == 0:
    return 0
  else:
    return 1/n + harmonicsum(n-1)
har5 = harmonicsum(0)
print(har5)  