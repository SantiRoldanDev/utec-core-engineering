#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])


if __name__ == "__main__":
    tuple_a = (1, 2)
    tuple_b = (3, 4)
    print(add_tuple(tuple_a, tuple_b))
