hight = float(input("Enter your hight"))
weight = float(input("Enter your weight"))
bmi=round(weight/hight**2, 2)
if bmi<18.5:
    print(f"your BMI is {bmi}, you are underweight")
elif bmi <25:
    print(f"your BMI is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"your BMI is {bmi}, you are slightlly over weight")
elif bmi < 35:
    print(f"your BMI is {bmi}, you are obese")
else:
    print(f"your BMI is {bmi}, you are clinically obese")