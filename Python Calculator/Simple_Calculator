print("Welcome to the Simple Calculator")

try:
    # Get the first and second numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter a valide numeric value.")
    exit() # Exits the program if input is invalid

# Get the operation to be performed
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation

if operation == '+':
    print("The result is:", num1 + num2) # Addition Statement
elif operation == '-':
    print("The result is:", num1 - num2) # Subtraction Statement
elif operation == '*': 
    # Rejects multiplying by 0 and informs users why
    if num1 == 0 or num2 == 0:
        print("Note: Multiplying by 0 will always result in 0.")
    print("The result is:", num1 * num2) # Multiplication Statement
elif operation == '/':
    if num1 == 0:
        print("Note: Dividing 0 by any number results in 0.")
    elif num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result is:", num1 / num2)
else:
    print("Error: Invalid operation. Please choose +, -, *, or /.")
