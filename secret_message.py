# Function to encrypt a message
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt a message
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            decrypted_char = chr((ord(char) - 65 - key) % 26 + 65)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Get message and key from user input
message = input("Enter the message to encrypt: ")
key = int(input("Enter the secret key (an integer): "))

# Encrypt the message
encrypted_message = encrypt(message, key)

# Display encrypted message
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)

# Display decrypted message
print("Decrypted message:", decrypted_message)
