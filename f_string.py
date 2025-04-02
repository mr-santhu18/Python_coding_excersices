''' age = int(input("enter your age :"))

years_left = 70-age
days_left = years_left*365
months_left = years_left*12
weeks_left = years_left*52

print(f"my age is {age}, and I  have {days_left} days ,{weeks_left} weeks and {months_left} months left") '''



# BMI PROBLEM


weight = int(input("enter your weight :"))
hight = float(input("enter your hight :"))

bmi = weight/ hight  ** 2

print(round(bmi))
if bmi< 18.5:
    print(f"your BMI is {bmi}, and you are underweight.")
elif bmi<25:
    print(f"your BMI is {bmi}, and you are normal weight.")
elif bmi<30:
    print(f"your BMI {bmi}, and you are over weight.")
else:
    print("your clinically obese.")
