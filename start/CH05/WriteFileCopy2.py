import os

script_path = os.path.realpath(__file__)
script_folder = os.path.split(script_path)

test_file = open(script_folder[0] + "/testfile.txt", "w")

test_file.write("Hello world\n")
test_file.write("\tanother line\n")
test_file.write("Last line\n")

test_file.close()