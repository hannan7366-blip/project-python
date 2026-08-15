name=input("enter your name")
marks=eval(input("enter your marks"))
total_marks=eval(input("enter total marks"))
percent=(marks/total_marks)*100
print("Name:",name)
print("Marks:",marks,"/",total_marks)
print("percentage:",round(percent,2),"%")
if (percent>= 90):
  print("grade : A+")
elif (percent>= 80):
  print("grade : A")
elif (percent>= 70):
  print ("grade : B")
elif (percent>= 60):
  print ("grade : C")
elif (percent>= 50):
  print ("grade : D")
else:
  print ("grade :F")
