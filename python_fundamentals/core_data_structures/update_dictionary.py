#!/usr/bin/env python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    my_dict = {"a": 1, "b": 2}
    print(update_dictionary(my_dict, "c", 3))
