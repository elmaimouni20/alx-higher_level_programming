#!/usr/bin/python3
i = 0
j = 0
while i < 9:
    j = i + 1
    while j < 10:
        print("{:s}{:s}".format(str(i), str(j)), end='')
        if i < 8:
            print(end=', ')
        j += 1
    i += 1
print(end='\n')
