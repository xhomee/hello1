print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

if height >= 120:
    print("Your a welcome!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket coasts 5$")
    elif age <= 18:
        print("Your ticket coasts 7$")
    else:
        print("Tour ticket costs 12$")

else:
    print("Your need to grou up)")