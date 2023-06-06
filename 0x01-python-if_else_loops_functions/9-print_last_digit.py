#!/usr/bin/python3
def print_last_digit(number):
    stri = str(number)
    last = stri[-1:]
    laststri = str(last)
    intl = int(last)
    print('{:d}'.format(intl), end='')
