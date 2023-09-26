# DATA TYPES
'''
two_digit_number = input("Type a two digit number: ")

print(int(two_digit_number[0]) + int(two_digit_number[1]))
'''

# BMI CALCULATOR
'''
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height = float(height)
weight = float(weight)

bmi = weight / (height * height)

print(round(bmi)) 
'''

# LIFE IN WEEKS
'''
age = input("What is your current age? ")

ageLeft = 90 - int(age)
print(f"You have {ageLeft * 365} days, {ageLeft * 52} weeks, and {ageLeft * 12} months left.")
'''

# TIP CALCULATOR
print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

totalBill += totalBill * percentage / 100

numberOfPeople = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round(totalBill / numberOfPeople, 2)}")
