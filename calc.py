# ********** A SIMPLE CALUCLATOR PROGRAM WITH NO USER INTERFACE **********


# Display an operation menu to the user
print('What do you want to do?')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('')

# capture the operation input from the user
operation = int(input('Type 1/2/3/4\n'))

# capture users 1st and 2nd number to perform math on
num1 = int(input('Enter first number\n'))
num2 = int(input('Enter second number\n'))

# check the operation input from the user and perform the math
if operation == 1:
    result = num1 + num2
    print(result)
elif operation == 2:
    result = num1 - num2
    print(result)
elif operation == 3:
    result = num1 * num2
    print(result)
elif operation == 4:
    result = num1 / num2
    print(result)

