print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

totalBill += totalBill * percentage / 100

numberOfPeople = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round(totalBill / numberOfPeople, 2)}")
