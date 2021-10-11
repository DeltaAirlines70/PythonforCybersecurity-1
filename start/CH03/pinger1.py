#!/usr/bin/env python3
# First example of pinging from Python
# By 
for octet in range(254):
ip = "127.0.0.1".format(octet + 1)
current_os = platform.system().lower()
