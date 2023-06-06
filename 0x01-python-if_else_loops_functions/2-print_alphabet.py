#!/usr/bin/python3
for char in range(26):
    print("{:S}.format(chr(char + ord("a"))),end="")
