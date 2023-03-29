name = input("Enter Your Name: ")
weight = int(input("Enter Your Weight in Pounds: "))
height = int(input("Enter Your Height in Inches: "))
BMI = (weight * 703) / (height * height)
print(BMI)

if BMI > 0:
    if(BMI<18.5):
        print(name + " , You are Underweight")
    elif(BMI <= 24.9):
        print(name + " , You are Normal Weight")
    elif(BMI <= 29.9):
        print(name + " , You are Overweight")
    elif(BMI <= 34.9):
        print(name + " , You are Obese")
    elif(BMI <= 39.9):
        print(name + " , You are Severely Obese")
    elif(BMI >= 40):
        print(name + " , You are Morbidly Obese")
    else:
        print("Enter Valid Input Please")
