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

def columnar_transposition_decrypt(ciphertext, num_columns, num_rows):
    #Performs columnar transposition decryption
    num_full_cols = len(ciphertext) % num_columns
    num_chars_in_short_cols = num_rows - 1
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    index = 0
    for col in range(num_columns):
        for row in range(num_rows if col < num_full_cols else num_chars_in_short_cols):
            if index < len(ciphertext):
                grid[row][col] = ciphertext[index]
                index += 1

    plaintext = "".join(grid[row][col] for row in range(num_rows) for col in range(num_columns) if grid[row][col])
    return plaintext

def decrypt(ciphertext, caesar_key1, caesar_key2, columnar_columns, num_rows):
    #Runs the decryption: Caesar -> Columnar Transposition -> Caesar
    step1 = caesar_cipher(ciphertext, caesar_key2, encrypt=False)
    step2 = columnar_transposition_decrypt(step1, columnar_columns, num_rows)
    final_plaintext = caesar_cipher(step2, caesar_key1, encrypt=False)
    return final_plaintext

# User input
ciphertext = input("Enter ciphertext: ")
caesar_key1 = input("Enter first Caesar cipher key (same as encryption): ")
caesar_key2 = input("Enter second Caesar cipher key (same as encryption): ")
columnar_columns = int(input("Enter number of columns for columnar transposition (same as encryption): "))
num_rows = int(input("Enter number of rows used in columnar transposition: "))

# Perform decryption
decrypted_text = decrypt(ciphertext, caesar_key1, caesar_key2, columnar_columns, num_rows)
print(f"\nDecrypted Text: {decrypted_text}")
