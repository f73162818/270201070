name = input("What is your name?")
for letter in name:
  letter = letter.upper()
  print(letter)

while True:
  q = input("Enter any string(quit to quit):")
  if q == 'quit':
    break
