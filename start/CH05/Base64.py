#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By 
import Base64

def encode_data(plain_text):
    plain_text = plain_text.encode()
    cipher_text = Base64.b64encode(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text
def decode_data(cipher_text):
    plain_text = Base64.b64decode(cipher_text)
    return plain_text

    method = input("Do you wish to Encode or Decode (e/d)? ")
    message = input("What is the message? ")

    if method[0] == "e":
        print(encode_data(message))
    elif method[0] == "d":
        print(decode_data(message))
    else:
        print("Wrong method selected. Choose Encode or Decode")