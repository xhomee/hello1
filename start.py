print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))
bill = 0

if height >= 120:
    print("Your a welcome!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket coasts 5$")
    elif age <= 18:
        bill = 7
        print("Youth ticket coasts 7$")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Youth ticket coasts 0$")
    else:
        bill = 12
        print("Adult ticket costs 12$")

    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")
