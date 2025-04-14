# Project 1 - Calculator

operator = input("Enter an operator (+, -, *, /, **): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    print(f"{num1 + num2}")
elif operator == "-":
    print(f"{num1 - num2}")
elif operator == "*":
    print(f"{num1 * num2}")
elif operator == "/":
    print(f"{num1 / num2}")
elif operator == "**":
    print(f"{num1 ** num2}")
else: 
    print("Please follow the instructions !")
