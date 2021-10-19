#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By 
from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    print("Key:", key.decode())

def encrypt(plain_text, key):
    plain_text = plain_text.encode()
    key = key.encode()
    cipher_text = Fernet(key).encrypt(plain_text)
    cipher_text = cipher_text.deocde()
    return cipher_text

def decrpyt(cipher_text, key):
    cipher_text = cipher_text.encode()
    key = key.encode()

    plain_text = Fernet(key).decrypt(cipher_text)
    plain_text = plain_text.decode()
    return plain_text
encKey = ""
print("What would you like to do")
method =  " " + input("Create(c), Encrpyt(e) or Decrypt(d)")
method = method[0].lower()
if method == " c":
    create_key()
elif method == " e":
    
    plain_text = input("Message to Encrypt or Decrypt")
 
    encKey = input("Encryption Key")
    cipher_text = encrypt(plain_text, encKey)
    print(cipher_text)

elif method == " d":

    cipher_text = input("Message to Encrypt or Decrypt")
    encKey = input("Decrpytion Key")
    plain_text = decrpyt(cipher_text, encKey)
    print(plain_text)
else:
    print("sorry, please enter c, d or r")
#if method != "c" and method != "d" and  method != "e":
  # d
  #       print("Sorry please enter c, e or d")
 