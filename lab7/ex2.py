def is_prime(a):
  if a <= 1:
    return False
  for i in range(2,a):
      if a%i == 0:
        return False
  return True

def print_primes_between(a,b):
  for i in range(a,b):
    if is_prime(i):
      print(i)
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
print_primes_between(a,b)


      