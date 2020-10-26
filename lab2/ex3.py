x=float(input("Enter your GPA:"))
y=float(input("Enter your Number of Lectures:"))

if x<2.0 and y<47 :
  print("Not enough number of lectures and GPA!")

elif x<2.0 and y>=47 :
  print("Not enough GPA!")

elif x>=2.0 and y<47 :
  print("Not enough number of lectures!")

elif x>2.0 and y>=47 :
  print("GRADUATED!!!")