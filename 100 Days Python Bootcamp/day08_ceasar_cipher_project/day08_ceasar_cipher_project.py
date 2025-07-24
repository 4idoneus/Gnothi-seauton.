# Ceasar Cipher Project
# This program allows users to encode or decode messages using a Ceasar cipher.
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(original_text,shift_amount,encode_or_decode):
    original_text = original_text.lower()
    crypt_msg =""
    if encode_or_decode == "decode":
       shift_amount *= -1
    for letter in range(len(original_text)):
        if original_text[letter] in alphabet:
            new_index = (alphabet.index(original_text[letter]) + shift_amount) % 26
            crypt_msg += alphabet[new_index]
        else:
            if original_text[letter] not in out_of_alphabet:
                print(f"The letter,{original_text[letter]} you used is not in our system. ")
                out_of_alphabet.append(original_text[letter])
            crypt_msg += original_text[letter]

    print(crypt_msg)
    restart_the_ceasar = input("Type 'yes' if you want to go again. Otherwise, type 'no'. ")

    if restart_the_ceasar.lower() == "yes":
        # restart = True
        return True
    elif restart_the_ceasar.lower() == "no":
        # restart = False
        return False
    else:
        print("You did not write the correct response. Program will be closing itself")
        return False


print(art.logo)
restart = True
out_of_alphabet = []
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    restart = ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)
print("Thank you for using our cypher program. May your text be always secret. ")