height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight/height**2)
print((bmi))
if bmi < 18.5:
  print("You are underweight")
  if bmi < 25:
    print("you are slightly overweight")
  elif bmi <30:
    print("you are obese")
  elif bmi <35:
    print("you are clinically obese")
else:
  print("they have normal weight")
  




