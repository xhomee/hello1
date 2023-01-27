#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters = 4
nr_symbols = 2
nr_numbers = 2


#add random letters
random_letters = []
for element in range(nr_letters):
    random_letters.append(random.choice(letters))
str_element_random_letters = ''
for element in random_letters:
    str_element_random_letters += element


#add random symbols
random_symbols = []
for element in range(nr_symbols):
    random_symbols.append(random.choice(numbers))
str_element_random_symbols = ''
for element in random_symbols:
    str_element_random_symbols += element


#add random numbers
random_numbers = []
for element in range(nr_symbols):
    random_numbers.append(random.choice(symbols))
str_element_random_numbers = ''
for element in random_numbers:
    str_element_random_numbers += element


# add shuffling to
x = []
b = []
c = ''
x.append(random_letters + random_symbols + random_numbers)
for element in x:
    b += element
random.shuffle(b)
for element in b:
    c += element


print(f"No shuffling: {str_element_random_letters}{str_element_random_symbols}{str_element_random_numbers}")
print(f"With shuffling: {c}")



password = []
for char in range(nr_letters):
    password.append(random.choice(letters))

for char in range(nr_symbols):
    password.append(random.choice(symbols))

for char in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
c_password = ''
for char in password:
    c_password +=char

print(f"With shuffling2: {c_password}")







