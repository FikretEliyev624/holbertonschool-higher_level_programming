#!/usr/bin/python3
for i in range(97, 123):   # a–z ASCII
    if i != ord('q') and i != ord('e'):
        print("{}".format(chr(i)), end="")
