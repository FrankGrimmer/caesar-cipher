# Dictionary Password Cracker - Frank Grimmer 2024

# Defines the characters for encryption/decryption.
letters = "abcdefghijklmnopqrstuvwxyz"
number_letters = 26  # Total number of letters in the alphabet.

# Function to encrypt or decrypt text using a Caesar cipher.
def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == "d":
        key = -key  # Invert the key for decryption mode.

    # Loop through each character in the text.
    for letter in text:
        letter = letter.lower()  # Convert character to lowercase.
        if letter != " ":  # Exclude spaces from encryption/decryption.
            index = letters.find(letter)  # Find the index of the letter in the alphabet.
            if index == -1:
                result += letter  # Append non alphabetic characters unchanged.
            else:
                new_index = (index + key) % number_letters  # Calculate the new index after shifting.
                result += letters[new_index]  # Append the new encrypted/decrypted character.
        else:
            result += " "  # Maintain spaces in the output.
    return result

# Function to only accept a cipher key that is within the length of the alphabet.
def get_valid_key():
    while True:
        try:
            key = int(input("Enter the cipher key (0-25): "))  # Get user input for the cipher key.
            if 0 <= key <= 25:
                return key  # Return the valid cipher key.
            else:
                print("Error: Please enter a number between 0 and 25.")
        except ValueError: # Handles the ValueError exception that occurs if the input cannot be converted to an integer.
            print("Error: Invalid input. Please enter a valid number.")

# Main function to run the Caesar Cipher Encryption/Decryption Tool.
def main():
    print("\nCaesar Cipher Encryption/Decryption Tool - Frank Grimmer 2024")

    # Creating a menu for the user to select an option. Will continue to run until user quits.
    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt an encrypted message")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")  # Prompt user for choice.

        if choice == "1":
            print("\nEncryption mode selected")
            key = get_valid_key()  # Get a valid cipher key from the user.
            text = input("Enter text to encrypt: ")  # Prompt user to enter text for encryption.
            ciphertext = encrypt_decrypt(text, "e", key)  # Encrypt the text.
            print(f"Cipher Text: {ciphertext}")  # Display the encrypted text.

        elif choice == "2":
            print("\nDecryption mode selected")
            key = get_valid_key()  # Get a valid cipher key from the user.
            text = input("Enter text to decrypt: ")  # Prompt user to enter text for decryption.
            plaintext = encrypt_decrypt(text, "d", key)  # Decrypt the text.
            print(f"Plain Text: {plaintext}")  # Display the decrypted text.

        elif choice == "3" or choice.lower() == "q": #Also enables the letter q to be used to quit.
            print("Exiting program. Goodbye!")
            break  # Exit the program if user chooses to quit.

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")  # Display error message for invalid input.

if __name__ == "__main__":
    main()  # Execute the main function only if this script is run directly.
