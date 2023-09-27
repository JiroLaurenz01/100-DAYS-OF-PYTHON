import random

# HEAD OR TAILS
'''=
randomValue = random.choice([True, False])
print("Heads" if randomValue else "Tails")
'''

# BANKER ROULETTE
'''
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(',')
indexValue = random.randint(0, len(names) - 1)

print(f"{names[indexValue].strip(' ')} is going to buy the meal today!")
'''

# TREASURE MAP
'''
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

map[int(position[1]) - 1][int(position[0]) - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
'''

# ROCK PAPER SCISSORS
choices = ["Rock", "Paper", "Scissors"]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computerChoice = random.randint(0, 2)

print(f"You chose: {choices[userChoice]}")
print(f"Computer chose: {choices[computerChoice]}")

if userChoice == computerChoice:
    result = "It's a tie!"
elif (userChoice == 0 and computerChoice == 2) or (userChoice == 1 and computerChoice == 0) or (userChoice == 2 and computerChoice == 1):
    result = "You win!"
else:
    result = "You lose!"

print(result)

