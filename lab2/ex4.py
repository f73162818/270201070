x=int(input("How old are you ?:"))
normal_price = 3
if x<6 or x>60 :
  ticket_price=free
  print(ticket_price)

elif 6<=x<=18 :
  discount=0.5
  print( normal_price * (1-discount))

else:
  print(normal_price)

