#https://ascii.co.uk/text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


def bluegate(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
#from art import logo
logo = """                                                                                                                                  
88888888ba  88                          ,ad8888ba,                                    ,ad8888ba,  88             88                                 
88      "8b 88                         d8"'    `"8b              ,d                  d8"'    `"8b ""             88                                 
88      ,8P 88                        d8'                        88                 d8'                          88                                 
88aaaaaa8P' 88 88       88  ,adPPYba, 88            ,adPPYYba, MM88MMM ,adPPYba,    88            88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88""""""8b, 88 88       88 a8P_____88 88      88888 ""     `Y8   88   a8P_____88    88            88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
88      `8b 88 88       88 8PP""""""" Y8,        88 ,adPPPPP88   88   8PP"""""""    Y8,           88 88       d8 88       88 8PP""""""" 88          
88      a8P 88 "8a,   ,a88 "8b,   ,aa  Y8a.    .a88 88,    ,88   88,  "8b,   ,aa     Y8a.    .a8P 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
88888888P"  88  `"YbbdP'Y8  `"Ybbd8"'   `"Y88888P"  `"8bbdP"Y8   "Y888 `"Ybbd8"'      `"Y8888Y"'  88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                                     88                                             
                                                    (Developed by Bluegate Solutions)                88       
"""

print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    bluegate(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")



