# Getting input as string and stripping whitespace
num1_input = input('Enter a number: ').strip()
operand = input('Enter a mathematical operator: ').strip()
num2_input = input('Enter another number: ').strip()

# Check for blank inputs
if not num1_input or not num2_input or not operand:
    print("Error: Inputs cannot be blank.")
    exit()

# Try converting to float
try:
    num1 = float(num1_input)
    num2 = float(num2_input)
except ValueError:
    print("Error: One or both inputs are not valid numbers.")
    exit()

# Try performing the operation
try:
    if operand == '+':
        result = num1 + num2
    elif operand == '-':
        result = num1 - num2
    elif operand == '*':
        result = num1 * num2
    elif operand == '/':
        if num2 == 0:
            raise ZeroDivisionError("You can't divide by zero.")
        result = num1 / num2
    elif operand == '%':
        if num2 == 0:
            raise ZeroDivisionError("You can't modulo by zero.")
        result = num1 % num2
    elif operand == '**':
        result = num1 ** num2
    else:
        raise ValueError("Invalid operation.")

    print(f"{num1} {operand} {num2} = {result}")

except ZeroDivisionError as zde:
    print("Math Error:", zde)
except ValueError as ve:
    print("Value Error:", ve)
