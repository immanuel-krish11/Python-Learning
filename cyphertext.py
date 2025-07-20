alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Input 'encode' to encrypt and 'decode' to decrypt: ")
text = input("Enter the text: ")
shift = int(input("Enter the shift value : "))

'''
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)  # 0-25 always
        cipher_text = cipher_text + alphabet[shifted_position]

    print("The encrypted text is : ", cipher_text)

def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position = shifted_position % len(alphabet)  # 0-25 always
        output_text = output_text + alphabet[shifted_position]

    print("The encrypted text is : ", output_text) '''

def caeser(original_text, shift_amount, directions):
    output_text = ""
    if directions == "decode":
        shift_amount = shift_amount * (-1)
    for letter in original_text:

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)  # 0-25 always
        output_text = output_text + alphabet[shifted_position]

    print("The cipher text is : ", output_text)

caeser(text, shift, direction)