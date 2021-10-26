#!/usr/bin/env python3
# Script that hashes a password
#By 

# Sample data
# Password: Password01
# Salt: G.DTW7g9s5U7KYf5
# SHA-512 result: $6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.
o = open("shadow.txt", "r")
for line in o:
# print the user from the shadow.txt and then print out the password from the top1000.txt