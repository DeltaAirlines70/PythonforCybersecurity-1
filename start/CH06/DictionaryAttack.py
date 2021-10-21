#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 
import crypt

def test_password(hashed_password, algorithm_salt, plaintext_password):
    crypted_password = crypt.crypt(plaintext_password, algorithm_salt)
    if hashed_password == crypted_password:
        return True
    return False

def read_dictionary(dictionary_file):
    f = open(dictionary_file, "r")
    message = f.read()
    return message

password_dictionary = read_dictionary("top10.txt")
hashed_password = input("What's the hashed password")
algorithm_salt = input("What is the algorithm and salt?")

for password in password_dictionary.splitlines():
    result = test_password(hashed_password, algorithm_salt, password)
    if result:
        print("Match found: {0}".format(password))
        break