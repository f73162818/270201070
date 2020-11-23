grades = [[50,90,60],[15,60,75],[99,95,91]]

for i in grades:
  mid1 = i[0]*30/100
  mid2 = i[1]*30/100
  final = i[2]*40/100
  average_grade = mid1 + mid2 + final
  print (average_grade)