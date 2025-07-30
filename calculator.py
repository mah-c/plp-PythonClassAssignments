num1 = float(input('Enter a number: '))
operand = input('Enter a mathematical operator: ')
num2 = float(input('Enter another number: '))

if operand == '+':
    result = num1 + num2
    print(num1, operand, num2, ' = ', result)
elif operand == '-':
    result = num1 - num2
    print(num1, operand, num2, ' = ', result)
elif operand == '*':
    result = num1 * num2
    print(num1, operand, num2, ' = ', result)
elif operand == '/':
    result = num1 / num2
    print(num1, operand, num2, ' = ', result)
elif operand == '%':
    result = num1 % num2
    print(num1, operand, num2, ' = ', result)
elif operand == '**':
    result = num1 ** num2
    print(num1, operand, num2, ' = ', result)
else:
    print('Invalid Operation')