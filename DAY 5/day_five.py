import random

# AVERAGE HEIGHT
'''
student_heights = [int(height) for height in input("Input a list of student heights ").split()]
heightSum = sum(student_heights)
print(round(heightSum // len(student_heights)))
'''

# HIGH SCORE
'''
student_scores = list(map(int, input("Input a list of student scores ").split()))
print(f"The highest score in the class is: {max(student_scores)}")
'''

# ADDING EVEN NUMBERS
'''
sum = 0
for i in range(2, 101, 2):
    sum += i

print(sum)
'''

# FIZZBUZZ
'''
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if not output:
        output = i
    print(output)
'''

# CREATE A PASSWORD
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numberOfLetters = int(input("How many letter would you like in your password? "))
numberOfSymbols = int(input("How many symbols would you like? "))
numberOfNumbers = int(input("How many numbers would you like? "))

passwordLength = numberOfLetters + numberOfSymbols + numberOfNumbers
passwordList = []

for _ in range(numberOfLetters):
    passwordList.append(random.choice(letters))

for _ in range(numberOfSymbols):
    passwordList.append(random.choice(symbols))

for _ in range(numberOfNumbers):
    passwordList.append(str(random.choice(numbers)))

random.shuffle(passwordList)
password = ''.join(passwordList)

print(password)
    

 
