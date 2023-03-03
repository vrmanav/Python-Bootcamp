
#! DAY 8 - Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("\n* WELCOME TO CAESAR CIPHER *")
print("  ------- -- ------ ------  ")
continue_again = True


def caesar_cipher(message, shift_num, decision):
    converted_text = ''
    if decision == 'decode':
        shift_num *= -1
    for char in message:
        if char in alphabet:
            alpha_index = alphabet.index(char)
            new_index = (alpha_index + shift_num) % 26
            new_alpha = alphabet[new_index]
            converted_text += new_alpha
        else:
            converted_text += char
    print(f"{decision}d text is - {converted_text}")


while continue_again:
    decision = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if decision == 'encode' or decision == 'decode':
        message = input("Type your message:\n").lower()
        shift_num = int(input("Type the shift number:\n"))
        caesar_cipher(message, shift_num, decision)
        do_continue = input("Do you want to continue again? [YES/NO]").lower()
        if do_continue == 'no':
            continue_again = False
            print("Goodbye. See You Soon!")
    else:
        print("Invalid Input Given. Have A Nice Day!")
        continue_again = False
