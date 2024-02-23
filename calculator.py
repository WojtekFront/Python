try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("The first number is not invalid. Please try again")
    exit()

try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("The second number is not invalid. Please try again")
    exit()

try:
    operator = str(input("Enter the operator (+,-,*,/): "))
except ValueError:
    print("The operator is not invalid. Please try again")
    exit()

if num1.empty() or num2.empty() or operator.empty():
    result = "incorrect input"
elif num1 == 0 or num2 == 0 or operator == 0:
    result = 0
elif operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":  
    if num2 == 0:
        print("Error:Division by zero.")
        exit()
    result = num1 / num2   
else:
    result = "incorrect value"
print(result)
