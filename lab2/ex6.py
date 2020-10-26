a=float(input("write a value for a:" ))
b=float(input("write a value for b:"))
c=float(input("write a value for c:"))

delta=b**2-4*a*c
root1=(-b-delta**0.5)/(2*a)
root2=(-b+delta**0.5)/(2*a)

if delta<0 :
  print("There are two complex roots.")
  print(root1 and root2)

elif delta==0 :
  print("There is one real root.")
  print(root1)

elif delta>0 :
  print("There are two real roots.")
  print(root1 and root2)