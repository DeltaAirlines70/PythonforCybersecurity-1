ip_file = open("ips.txt", "r")
for line in ip_file:
    if line.startswith("192."):
        print(line)
    ip_file.close()