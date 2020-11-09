a = int(input("Enter a number:"))
b = int(input("Enter a power:"))
result = 1

for number in range(1,b+1):
  result *= a
print (result)
