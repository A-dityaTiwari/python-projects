#python calculator
operator = input("Enter an operator (+ - * /): ")
first_number = float(input("Enter the first number : "))
second_number = float(input ("Enter the second number : "))

if operator not in ['+','-','*','/']:
    print(f"{operator} is not a valid operator")
elif operator == "+":
    result = first_number + second_number
    print (round(result , 3))
elif operator == "-":
    result = first_number - second_number
    print (round(result , 3))
elif operator == "*":
    result = first_number*second_number
    print (round(result , 3))
elif operator == "/":
    if second_number == 0:
        print("Error: Cannot divide my zero")
    result = first_number / second_number
    print (round(result , 3))
else:
    print(f"{operator} is not a valid operator")

