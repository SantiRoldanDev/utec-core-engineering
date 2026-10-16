#!/usr/bin/env python3

def pow(a, b):
    contador = 0
    while contador < b:
        a *= a
        contador += 1
    return a
