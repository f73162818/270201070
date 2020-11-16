a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
matching_digits = 0
while a > 0 and b > 0 :
  if a%10 == b%10:
   matching_digits += 1
  a//= 10
  b//= 10
print (matching_digits)



