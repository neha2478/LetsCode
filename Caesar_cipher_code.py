#------------------------CYSER CYPHER ENCODING------------------------------------------------------

#Import the logo of caesar cipher 
import Art

print(Art.logo)

#This is the part
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))
'''

'''
# TODO-1 : Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount" as 2 inputs.

def encrypt(original_text, shift_amount):
    cipher_text = "" #j

    #hello 2
    # TODO-2 : Inside the 'encrypt() function, shift each letter of the 'original_text' towards in the alphabet by the 'shift_amount' and print the encrypted text.
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount  #7 -> 9

        # TODO-4 : What happens if you try to shift z forwards by 9? Can you fix the code?
        shifted_position %= len(alphabet) # 0 - 25 , even if it exceeds the then 

        cipher_text += alphabet[shifted_position]  #j

    print(f"Here is the encoded result: {cipher_text}")
        

# TODO-3 : Call the encrypt() function and pass the user inputs. You should be able to test the code and encrypt
encrypt(original_text = text, shift_amount = shift)


#DECRYPTION :- hence decoding the text

# TODO-5 :- Create a function called decrypt() that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-6 :- Inside the 'decrypt()' function, shift each letter of the 'original_text' forwards in the alphabet 
# backwards by the shift_amount and print  the decrypted text

def decrypt(original_text, shift_amount):
    op_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        op_text += alphabet[shifted_position]        

    print(f"Here is the decoded result: {op_text}")


decrypt(original_text=text, shift_amount=shift)

'''

#TODO-3:- Combine the 'encrypt()' and 'decrypt()' functions into one function called caesar().
#Use the value of the user chosen direction variable to determine which functionality to use.
#Call the caesar function instead of encrypt/decrypt and pass in all three variables direction/ text/shift.
'''
def caesar(original_text, shift_amount , encode_or_decode):
    cipher_text = ""

    for letter in original_text: # type: ignore
        if encode_or_decode == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
        else:
            shifted_position = alphabet.index(letter) + shift_amount
        
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result: {cipher_text}")

#calling the function 
caesar(original_text=text, shift_amount=shift , encode_or_decode=direction)
'''

#another logic
'''
for letter in original_text: # type: ignore
        if encode_or_decode == "decode":
           shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result: {cipher_text}")
'''


# Reorganising our Code
# TODO-1 : Import and print the logo from art.py when the program starts.
# TODO-2 : What happens if the user enters a number/symbol/space?
# TODO-3 : Can you figure out a way to restart the cipher program?
def caesar(original_text, shift_amount , encode_or_decode):
    output_text = ""

    for letter in original_text: # type: ignore
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
        
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")