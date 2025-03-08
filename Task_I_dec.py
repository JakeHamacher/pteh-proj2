import string

def decryption(ciphertext, offset):
    upper = string.ascii_uppercase
    numbers = string.digits
    plaintext = ""

    ciphertext = ciphertext.upper()

    for char in ciphertext:
        if char in upper:
            index = (upper.index(char) - offset) % 26
            plaintext += upper[index]
        elif char in numbers:
            plaintext += char
        else:
            continue

    return plaintext

print("--------------- Decryption ---------------")
ciphertext = input("Enter the Ciphertext: ")
offset = input("Enter the offset: ")
offset = int(offset)

plaintext = decryption(ciphertext, offset)
print("\nPlaintext:", plaintext)