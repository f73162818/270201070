employees = {}
for i in range(5):
  a = input("Enter your name:")
  b = input("Enter your salary:")
  employees[b] = (a)
salaries = list(employees.keys)
salaries = sorted(salaries, reverse=True)
for j in range(3):
 print(employees[salaries[j]])