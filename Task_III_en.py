# Student Name:  Jacob Hamacher
# Program Name:  Task 3 Encryptor
# Creation Date:  3/9/25
# Last Modified Date:  4/7/25(Adding comments)
# CSCI Course:  CSCI 452
# Grade Received:  --/100 (Pending grade)
# Design Comments: This is a python program that takes in a 
#                  plaintext message, two cipher keys, and a 
#                  value to perform the columnar shift. It is
#                  meant to be paired with the Decryptor from
#                  task 3.

import math

def caesar_cipher(text, key, encrypt=True):
    #Performs a Caesar cipher
    key = key.upper()
    key_length = len(key)
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            if not encrypt:
                shift = -shift
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def columnar_transposition_encrypt(text, num_columns=6):
    #Performs columnar transposition encryption
    text = text.replace(" ", "")
    num_rows = math.ceil(len(text) / num_columns)

    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for row in range(num_rows):
        for col in range(num_columns):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1

    cipher_text = ""
    for col in range(num_columns):
        for row in range(num_rows):
            if grid[row][col]:
                cipher_text += grid[row][col]

    return cipher_text, num_rows

def encrypt(text, caesar_key1, caesar_key2, columnar_columns):
    #Runs the encryption: Caesar -> Columnar Transposition -> Caesar
    step1 = caesar_cipher(text, caesar_key1, encrypt=True)
    step2, num_rows = columnar_transposition_encrypt(step1, num_columns=columnar_columns)
    final_cipher = caesar_cipher(step2, caesar_key2, encrypt=True)
    return final_cipher, num_rows

# User input
plaintext = input("Enter plaintext: ")
caesar_key1 = input("Enter first Caesar cipher key: ")
caesar_key2 = input("Enter second Caesar cipher key: ")
columnar_columns = int(input("Enter number of columns for columnar transposition: "))

# Perform encryption
ciphertext, num_rows = encrypt(plaintext, caesar_key1, caesar_key2, columnar_columns)
print(f"\nEncrypted Text: {ciphertext}")
print(f"Number of rows used in columnar transposition: {num_rows}")
