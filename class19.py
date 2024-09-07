

def add(a,b):
    return print(a+b)

def sub(a, b):
    response =  input('Do you wanna do Bigger Number - Smaller number? Type Y for Yes and N for No: \n')
    if response == 'Y':
        if a> b:
            return a-b
        elif b>a:
            return b-a
        elif a==b:
            return print(0)
    elif response == 'N':
        return a - b

def multi(a, b):
    return a*b

def div(a, b):
    if b!= 0: # B is not equals to zero
        return print(a/b)
    else:
        print('You cannot divide a number by zero')

    if b == 0:
        print('You can not divide a number by zero')
    else:
        return a/b


print('Select an operation')
print('1. Addition')
print('2. Subtraction')
print('3 Multiplication')
print('4. Division')

while True:
    a= int(input('Enter the first number'))
    b = int(input('Enter the second number'))
    choice = input('Enter your choice: \n type 1 for Addition \n type 2 for Subtraction \n type 3 for multiplication \n type 4 for division')
    if choice == '1':
        print(f'{a} + {b} = {add(a, b)}')
    if choice == '2':
        print(f'{a} - {b} = {sub(a, b)}')
    if choice == '3':
        print(f'{a} * {b} = {multi(a, b)}')
    if choice == '4':
        print(f'{a} / {b} = {div(a, b)}')
    cancel = input('Do you want to continue Type Y/N')
    if cancel == 'N':
        break