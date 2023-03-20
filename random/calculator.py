# Build a calculator

num1 = input('Enter first integer: ')
operation = input('Enter operation to perform(+,-,*,/,%,//): ')
num2 = input('Enter second integer: ')

def calculator(num1, operation, num2):
    int1 = float(num1)
    int2 = float(num2)

    # Check if operand is valid then operate
    if(operation == '+'):
        return int1 + int2
    elif(operation == '-'):
        return int1 - int2
    elif(operation == '*'):
        return int1 * int2
    elif(operation == '/'):
        return int1 / int2
    elif(operation == '%'):
        return int1 % int2
    elif(operation == '//'):
        return int1 // int2
    else:
        return 'Entered operand is not valid'
    
print(calculator(num1, operation, num2))