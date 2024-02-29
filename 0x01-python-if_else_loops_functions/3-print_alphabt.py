#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    else:
        print("{:s}".format(chr(i)), end='')
