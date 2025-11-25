#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for el in my_list:
        if el not in unique:
            unique.append(el)
    return sum(unique)
