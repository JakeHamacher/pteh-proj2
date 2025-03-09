def decrypt(cipher_text, columns):

    text = ""
    for char in cipher_text:
        if char.isalpha(): 
            text += char.upper()
    
    rows = (len(text) + columns - 1) // columns
    

    plain_text = [''] * len(text) 

    index = 0
    for col in range(columns):
        for row in range(rows):
            if index < len(text):  
                pos = row * columns + col
                if pos < len(plain_text):
                    plain_text[pos] = text[index]
                    index += 1
    
    return ''.join(plain_text)

print("--------------- Decryption ---------------")
cipher_text = input("Enter the ciphertext: ")
columns = 6
plain_text = decrypt(cipher_text, columns)
print("\nYour plaintext:", plain_text)