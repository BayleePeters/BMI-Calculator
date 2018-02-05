weight = input("What is your weight? ")
height = input("What is your height? ")

BMI = 703*(int(weight)/int(height)**2)

print("Your BMI is "+ str(BMI) + ".")

if ((BMI) <= 18):
	print ("You are underweight.")
elif(((BMI) > 18) and ((BMI) < 26)):
	print ("Your weight is normal.")
else:
	print ("You are overwight.")