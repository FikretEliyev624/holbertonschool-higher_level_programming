#!/usr/bin/python3
def common_elements(set_1, set_2):
    for el in set_1 & set_2:
        return el
