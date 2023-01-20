print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

sum_all = round((bill + (bill/100*tip)) / people,2)

print(f"Each person should pay: ${sum_all}")