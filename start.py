from pi_module import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(text_t, shift_t, direction_t):
    end_text = ""
    for letter in text_t:
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            if direction_t == "encode" or direction_t == "e":
                if position + shift_t > 25:
                    new_position = (position + shift_t) - 26
                else:
                    new_position = position + shift_t
            elif direction_t == "decode" or direction_t == "d":
                if position - shift_t < 0:
                    new_position = (26 + (position - shift_t))
                else:
                    new_position = position - shift_t
            else:
                print("I dont know this comand")

            new_letter = alphabet[new_position]
            end_text +=new_letter
    print(f"The {direction_t} text is: {end_text}")
    print("")


code_working = True
while code_working:
    direction = input("Type 'encode or e' to encrypt, type 'decode or d' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    if shift > 26 :
        x = shift % 26
    else:
        x = shift
    caesar(text_t=text, shift_t=x, direction_t=direction)

    end = input("Type 'yes or y' if you want to go again. Otherwise type 'no or n'.\n").lower()
    if end == "yes" or end == "y":
        pass
    elif end == "xhomee":
        print("Your a god")
        pass
    else:
        code_working = False
        print("Good Bye")

