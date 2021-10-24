#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By 
# Asks for the message you want to encrypt or decrypt
source_message = input("What is your message to encrypt/decrypt?")
source_message = source_message.lower()
final_message = ""

for letter in source_message:
    # reads through the line and converts the letters into ascii_num
    ascii_num = ord(letter)
    if ascii_num >= 97 and ascii_num <= 122:
    # Converts ascii_num to new_ascii
        new_ascii = ascii_num + 13
        if new_ascii > 122:
            new_ascii = new_ascii - 26
    # Converts the new_ascii  into a final message
    final_message = final_message + chr(new_ascii)
else:
      final_message = final_message + chr(ascii_num)
    # prints the final message
print("Message to be converted")
print(final_message)
