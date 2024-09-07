# check if the first and the last numbers of a list are same
# Check if a number is divisible by 5 or not
# Check if a number is palindrome or not
# Find the HCF of two numbers 

def same():
    x = [12,484,8445,12,8488,56,81]
    print(x[0])# first number
    print(x[-1])# Last number
    first_number = x[0]
    last_number = x[-1]
    if first_number == last_number:
        print(f'{first_number}, {last_number} are same')
    else:
        print(f'{first_number}, {last_number} are not same')

# check if a number is divisible by 5 or not
def divide_5():
    number = int(input('Enter a number'))
    if number % 5 == 0:
        print(f'{number} is divisible by 5')
    else:
        print(f'{number} is not divisible by 5')

