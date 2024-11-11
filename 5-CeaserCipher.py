from art import *

print(text2art("Caeser Cipher"))

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(original_text, shift_amount):
    final_text = ""

    for i in original_text:
        if type(i) != str or i == " ":
            final_text += i
        else:
            initial_position = alphabet.index(i)
            if (initial_position + shift_amount) > len(alphabet) - 1:
                final_position = initial_position + shift_amount - len(alphabet)
            else:
                final_position = initial_position + shift_amount
            final_text += alphabet[final_position]

    print(f"Here is the encoded result: {final_text}")

def decrypt(original_text, shift_amount):
    final_text = ""

    for i in original_text:
        if type(i) != str or i == " ":
            final_text += i
        else:
            final_position = alphabet.index(i)
            if (final_position - shift_amount) < 0:
                initial_position = final_position - shift_amount + len(alphabet)
            else:
                initial_position = final_position - shift_amount
            final_text += alphabet[initial_position]
    
    print(f"Here is the decoded result: {final_text}")

def caeser():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        encrypt(text, shift)
    
    elif direction == "decode":
        decrypt(text, shift)

    go_again = input("Type 'yes' if you wanna go again. Otherwise type 'no'.\n")
    
    if go_again == "yes":
        caeser()
    else:
        exit


caeser()
