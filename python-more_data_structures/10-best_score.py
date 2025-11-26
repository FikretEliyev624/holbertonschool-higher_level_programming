#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_val = 0
    best_key = None

    for key, value in a_dictionary.items():
        if value > best_val:
            best_val = value
            best_key = key

    return best_key
