#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(a + b for a, b in zip(tuple_a, tuple_b))


if __name__ == "__main__":
    tuple_a = (1, 2)
    tuple_b = (3, 4)
    print(add_tuple(tuple_a, tuple_b))