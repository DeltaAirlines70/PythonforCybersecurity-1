import os
script_path = os.path.realpath(__file__)
script_folder = os.path.split(script_path)
test_file = open(script_folder[0] + "/testfile.txt", "w")
test_file.write("Grapes\n")
test_file.write("\tGumballs\n")
test_file.write("Greenwood\n")
test_file.close()