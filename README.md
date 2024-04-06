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
```bash
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
