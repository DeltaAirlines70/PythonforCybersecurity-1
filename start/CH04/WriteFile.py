test_file = open("hackme.txt", "w") 
print("What is your name?")
name = input()
print("What is your favorite color?")
color = input()
print("What was the name of your first pet you had?")
petsname = input()
print("What is your mother's maiden name")
maidename = input()
print("What elementary school did you attend")
elementaryschool = input()
print("Your name is " + name)
test_file.write("Your name is " + name + "\n") 
print("Your favorite color is " + color)
test_file.write("Your favorite color is " + color + "\n")
print("the name of your first pet is " + petsname)
test_file.write("The name of the first pet I had is " + name + "\n")
print("Your mother's maiden name is " + maidename)
test_file.write("My mother's maiden name is " + maidename + "\n")
print("The elementary school I attended was " + elementaryschool)
test_file.write("The elementary school I attened was " + elementaryschool + "\n")
test_file.close()