#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for val in my_list:
        result.append(True if val % 2 == 0 else False)
    return result
