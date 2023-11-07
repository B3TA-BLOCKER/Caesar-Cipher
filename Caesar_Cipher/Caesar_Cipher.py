alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']


# Importing and printing the logo from art.py when the program starts.
from art import logo
print(logo)

def caesar(start_text , shift_amount,cipher_direction):
    end_text =""
    if shift_amount>26:
        shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # What happens if the user enters a number/symbol/space?
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else :
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}") 


# If the user wants to restart the cipher program?
should_repeat = True
while should_repeat:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
    text = input("Type your Message : \n").lower()
    shift = int(input("Type the shift number : \n"))

    caesar(start_text=text , shift_amount=shift , cipher_direction=direction)

    result = input("Type 'yes' if you want to go again, Otherwise type 'no'  : \n ").lower()

    if result == "no":
        should_repeat = False 