# Brute Force Decryption for Caesar Cipher - Frank Grimmer 2024

def decrypt_brute_force(ciphertext):
    letters = "abcdefghijklmnopqrstuvwxyz"
    number_letters = len(letters)
    
    # Try all possible keys (0 to 25).
    for key in range(number_letters):
        plaintext = ""
        for letter in ciphertext.lower():
            if letter in letters:
                index = letters.find(letter)
                new_index = (index - key) % number_letters
                plaintext += letters[new_index]
            else:
                plaintext += letter
        print(f"Key {key}: {plaintext}")


print("\nBrute Force Decryption for Caesar Cipher - Frank Grimmer 2024")

# User enters the ciphertext.
user_ciphertext = input("\nEnter ciphertext to decrypt: ")

# Perform brute force decryption.
print("Attempting brute force decryption...")
decrypt_brute_force(user_ciphertext)
