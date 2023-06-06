#!/usr/bin/python3
def uppercase(str):
    for _ in str:
        if ord(_) >= 97 and ord(_) <= 123:
            _ = chr(ord(_) - 32)
        print("{}".format(_), end="")
    print()
