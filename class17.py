# write a python program to calculate the BMI of a person
# write a program to calculate you age. 
# write a program that finds out whether a year is a leap year or not.

def bmi_cal():
    weight = float(input('Enter your Weight in Kilograms'))
    height = float(input('Enter your height in meters'))

    BMI = weight/(height*height)
    print(BMI)
    if BMI <18.5:
        print('The person is underweight and your BMI is ', BMI)
    if BMI>= 18.5 and BMI <24.9:
        print('the person is normal and the BMI is ', BMI)
    if BMI >=25 and BMI <29.9:
        print('The person is overweight and BMI is ', BMI)
    if BMI >=30 and BMI < 34.9:
        print('The person is Obese and BMI is ', BMI)
    if BMI > 35:
        print('The person is exteremly obese and the BMI is ', BMI)

#bmi_cal()

def leap_year():
    print('Find out whether an year is a leap year or not. ')
    year = int(input('Enter the year\n'))
    # if an year is divisible by 100 and 400 its a leap year
    # if an year is divisible by 4 and not by 100  then its a leap year
    # else its not a leap year

    if (year % 100 ==0) and (year % 400 == 0):
        print(year, ' is a century year and a leap year')
    if (year % 4 == 0) and (year % 100 != 0):
        print(year, ' is a leap year and not a century year')
    else:
        print(year, ' is not a leap year')
leap_year()