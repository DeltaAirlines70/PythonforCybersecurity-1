#!/usr/bin/env python3
# Sample script that writes to a file
# By 
# Intro to cryptography
# How cryptography *can work* - ROT13
test_file = open("hackme.txt", "w") 
#print("What is your name?")
#name = input()
#print("What is your favorite color?")
#color = input()
#print("What was the name of your first pet you had?")
#petsname = input()
#print("What is your mother's maiden name")
#maidename = input()
#print("What elementary school did you attend")
#elementaryschool = input()
test_file.write("Your name is")
test_file.write("Your favorite color is ")
test_file.write("The name of the first pet I had is ")
test_file.write("The elementary school I attened was")
test_file.write("My mother's maiden name is ")
test_file.close()
