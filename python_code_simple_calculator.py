x= eval(input("enter a number (x)"))
y= eval(input("enter another number (y)"))
print ("enter your choice")
print ("1 for addition")
print ("2 for subtraction")
print ("3 for multiplycation")
print ("4 for division")
choice=eval(input("enter your choice"))
if (choice == 1):
  z=x+y
  print(z)
elif (choice == 2 ):
  z=x-y
  print(z)
elif (choice == 3):
  z=x*y
  print(z)
elif (choice == 4):
  z=x/y
  print(z)
else:
  print("wrong input")
