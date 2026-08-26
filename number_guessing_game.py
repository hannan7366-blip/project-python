import random
lower_limit=int(input("enter lower limit"))
upper_limit=int(input("enter upper limit"))
number = random.randint(lower_limit,upper_limit)
x = int(input("guess the number"))
if x == number :
  print("correct answer")
else:
  print("incorrect answer")
  
