import string

def encryption(plaintext, offset):
    upper = string.ascii_uppercase
    numbers = string.digits
    ciphertext = ""

    plaintext = plaintext.upper()

    for char in plaintext:
        if char in upper:
            index = (upper.index(char) + offset) % 26
            ciphertext += upper[index]
        elif char in numbers:
            ciphertext += char
        else:
            continue

    return ciphertext

print("--------------- Encryption ---------------")
plaintext = input("Enter the Plaintext: ")
offset = input("Enter the offset: ")
offset = int(offset)

ciphertext = encryption(plaintext, offset)
print("\nCiphertext:", ciphertext)