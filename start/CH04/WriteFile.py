#!/usr/bin/env python3
# Sample script that writes to a file
# By 
# Intro to cryptography
# How cryptography *can work* - ROT13

print("What is your name?")
name = input()
test_file.write("Your name is", name)
print("What is your favorite color?")
color = input()
test_file.write("Your favorite color is ", color)
print("What was the name of your first pet you had?")
petsname = input()
test_file.write("The name of your first pet you had is ", petsname)
print("What is your mother's maiden name")
maidename = input()
test_file.write("My mother's maiden name is ", maidename)
print("What elementary school did you attend")
elementaryschool = input()
test_file.write("The elementary school I attened was", elementaryschool)
test_file = open("hackme.txt", "w") 
test_file.close()
