# Caesar Cipher Encryption/Decryption Tool

This tool allows you to encrypt and decrypt messages using a Caesar cipher. It provides a command-line interface (CLI) with a menu for selecting encryption or decryption operations.

## Features

- Encrypt a plaintext message using a specified cipher key.
- Decrypt an encrypted message using the corresponding cipher key.
- Supports encryption/decryption for alphabetic characters (a-z) while preserving spaces.

## Requirements

- Python 3.x installed on your system.

## Usage

1. Clone the repository or download the `caesar_cipher.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `caesar_cipher.py`.
4. Run the script by executing the following command:

   ```bash
   python caesar_cipher.py

## Example
```
$ python caesar_cipher.py

Caesar Cipher Encryption/Decryption Tool - Frank Grimmer 2024

Menu:
1. Encrypt a message
2. Decrypt an encrypted message
3. Quit

Enter your choice (1/2/3): 1

Encryption mode selected
Enter the cipher key (0-25): 3
Enter text to encrypt: hello world
Cipher Text: khoor zruog

Menu:
1. Encrypt a message
2. Decrypt an encrypted message
3. Quit

Enter your choice (1/2/3): 2

Decryption mode selected
Enter the cipher key (0-25): 3
Enter text to decrypt: khoor zruog
Plain Text: hello world

Menu:
1. Encrypt a message
2. Decrypt an encrypted message
3. Quit

Enter your choice (1/2/3): 3

Exiting program. Goodbye!
```
# Exploit: Brute Force Attack on Caesar Cipher

The Caesar cipher, while historically significant, is a very weak form of encryption by modern standards. It is vulnerable to brute force attacks due to its limited key space (only 26 possible keys) and predictable nature. Here's how a brute force attack can be used to decrypt a message encrypted with a Caesar cipher:

## Understanding the Caesar Cipher

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a fixed number of positions down or up the alphabet. For example, with a shift of 3 (key = 3), 'A' becomes 'D', 'B' becomes 'E', and so on.

## Brute Force Decryption

To exploit the Caesar cipher using brute force:

1. **Try All Possible Keys**: The attacker tries every possible key (0 to 25) to decrypt the ciphertext.
2. **Decrypt Using Each Key**: For each key, the attacker applies the decryption function to the ciphertext.
3. **Evaluate Decryption Results**: The attacker analyzes the decrypted text for meaningful output (e.g., English words or phrases).

## Brute Force Decryption for Caesar Cipher

The `brute-force-caesar.py` script provides a function (`decrypt_brute_force`) to demonstrate the vulnerability of the Caesar cipher by attempting brute force decryption.

### Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory containing `brute-force-caesar.py`.
4. Run the script by entering the following command:

   ```bash
   python brute-force-caesar.py

### Example
Suppose you have a ciphertext khoor zruog that you want to decrypt. You can run the script, provide this ciphertext as input, and observe the output as the script attempts to decrypt it using different keys.
```
Enter ciphertext to decrypt: khoor zruog
Attempting brute force decryption...
Key 0: khoor zruog
Key 1: jgnnq yqtnf
Key 2: ifmmp xpsme
Key 3: hello world
Key 4: gdkkn vnqkc
...
```
This demonstrates how the Caesar cipher's simplicity can lead to vulnerability when subjected to a brute force attack.

## License

This project is licensed under the [MIT License](LICENSE).
