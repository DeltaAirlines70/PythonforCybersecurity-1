#!/usr/bin/env python3
# Sample script that writes to a file
# By 
# Intro to cryptography

# How cryptography *can work* - ROT13
test_file = open("testfile.txt", "w")
test_file.write("Hello World")
test_file.write("My name is Ed\n")
test_file.write("I like rubber ducks\n")

test_file.close()
