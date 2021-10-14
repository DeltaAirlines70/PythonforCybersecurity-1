#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By 
import platform
import os
from datetime import datetime

def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    f = open("pinger.log","a")
    f.write(message)
    f.close()

def ping_host(ip):
    currrent_os = platform.system
    if currrent_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
     ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/nul 2>&1"
    exit_code = os.sytem(ping_cmd)
    return exit_code

def import_addresses():
    lines = []
    f = open("ips.txt", "r")
    for line in f:
        line = line.strip()
        lines.append(line)
    return lines
write_log("Read IPS from ips.txt")
ip_addresses = import_addresses()
write_log("Imported {0} IPS".format(len(ip_addresses)))

for ip in ip_addresses:
    exit_code = ping_host(ip)

    if exit_code == 0:
        write_log("{0} is online".format(ip))
        print("{0} is online".format(ip))
    else:
        print("{0} is offline".format(ip))