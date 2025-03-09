def encrypt(plain_text, columns):
    # Remove speccial character and make upercase letter
    cleaned_text = ""
    for char in plain_text:
        if char.isalpha():  
            cleaned_text += char.upper() 
    
    rows = (len(cleaned_text) + columns - 1) // columns
    #array place holder for plaintext
    ciphertext = []
    
    for col in range(columns):
        for row in range(rows):
            index = row * columns + col 
            if index < len(cleaned_text): ciphertext.append(cleaned_text[index])
    return ''.join(ciphertext)

print("--------------- Encryption ---------------")
plain_text = input("\nEnter the plaintext: ")
columns = 6
ciphertext = encrypt(plain_text, columns)
print("\nYour ciphertext:", ciphertext)