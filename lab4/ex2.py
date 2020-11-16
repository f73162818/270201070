N = int(input("Enter a number:"))
even_num = 0
for i in range(1,N+1):
  number = int(input("Please enter an integer:"))
  if number%2 == 0:
   even_num += 1
print((even_num / N)*100 , "%" )


