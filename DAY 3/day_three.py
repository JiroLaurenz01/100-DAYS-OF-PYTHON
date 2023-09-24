# ODD OR EVEN
'''
number = int(input("Which number do you want to check? "))

print(f"This is an {'even' if number % 2 == 0 else 'odd'} number.")
'''

# BMI CALCULATOR
'''
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    result = "are underweight"
elif bmi < 25:
    result = "have a normal weight"
elif bmi < 30:
    result = "are slightly overweight"
elif bmi < 35:
    result = "are obese"
else:
    result = "are clinically obese"

print(f"Your BMI is {bmi}, you {result}.")
'''

# LEAP YEAR
'''
year = int(input("Which year do you want to check? "))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Leap year" if isLeapYear else "Not leap year.")
'''

# PIZZA ORDER
'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
bill += (25 if (size == 'L') else (20 if (size == 'M') else 15))
bill += (2 if (size == 'S' and add_pepperoni == 'Y') else (3 if (add_pepperoni == 'Y') else 0))
bill += (1 if (extra_cheese == 'Y') else 0)

print(f"Your final bill is ${bill}.")
'''

# LOVE CALCULATOR
'''
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedName = (name1 + name2).lower()
toCheck = "truelove"
points = 0

for i, letter in enumerate(toCheck):
    if (i == 4):
        points *= 10

    points += combinedName.count(letter)

if points < 10 or points > 90:
    print(f"Your score is {points}, you go together like coke and mentos.")
elif 40 <= points <= 50:
    print(f"Your score is {points}, you are alright together.")
else:
    print(f"Your score is {points}.")
'''

# TREASURE ISLAND
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

while True:
    choiceOne = input('You\'re at a crossroad, where do you want to go? Type "left" or right": ').lower()

    if choiceOne == "left":
        break          
    elif choiceOne == "right":
        print("You fell into a hole. Game Over.")
        raise SystemExit
    else:
        print("Wrong input.")

while True:
    choiceTwo = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross: ').lower()

    if choiceTwo == "wait":
        break
    elif choiceTwo == "swim":
        print("You got attacked by an angry trout. Game Over.")
        raise SystemExit
    else:
        print("Wrong input.")

while True:
    choiceThree = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose: ").lower()
    
    if choiceThree == "red":
        print("It's a room full of fire. Game Over.")
        raise SystemExit
    elif choiceThree == "blue":
        print("You enter a room of beasts. Game Over.")
        raise SystemExit
    elif choiceThree == "yellow":
        print("You found the treasure! You Win!")
        break
    else:
        print("Wrong input.")











