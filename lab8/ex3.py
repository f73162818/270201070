def get_evens_recursive(l,c=0):
  if len(l) == 0:
    return c
  current = l.pop()
  if current % 2 == 0:
    c+=1
  return get_evens_recursive(l,c)

def get_evens(l):
  return get_evens_recursive(l,c=0)
    
print(get_evens([0,1,2,3,4,5]))