
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]


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

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    bluegate(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

# For any feedback or comment kindly contact bluegate.log@gmail.com
# Thank you for your time and support



