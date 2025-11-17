#!/usr/bin/python3
def uppercase(string):
    for c in string:
        print(
            "{}".format(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c),
            end=""
        )
    print("")

