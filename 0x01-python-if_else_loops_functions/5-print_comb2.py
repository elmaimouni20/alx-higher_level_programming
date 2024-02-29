#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{:s}".format(str(i).zfill(2)), end='\n')
    else:
        print("{:s}".format(str(i).zfill(2)), end=', ')
