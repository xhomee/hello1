from pi_module import logo

print(logo)
check_dict = []

poll = True
while poll:
    your_name = input("What is your name?: ")
    your_price = int(input("What is your bid?: "))

    def check_biggest(you_name, you_price):
        add_dict = {"name": you_name, "price": you_price}
        check_dict.append(add_dict)


    check_biggest(you_name=your_name, you_price=your_price)
    end_poll = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if end_poll == "n" or end_poll == "no":
        big = 0
        name = ""
        for biggest_value in check_dict:
            if biggest_value["price"] > big:
                big = biggest_value["price"]
                name = biggest_value["name"]
        print(f"The winner is {name} with a bid of ${big}")
        poll = False
