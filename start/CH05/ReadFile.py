import os
script_path = os.realpath(__file__)
script_folder = os.path.split(script_path)
ip_file = open(script_folder[0]+ "/ips.txt", "r")
ip_addresses = ip_file.read()
print(ip_addresses)

ip_file.close()