#!/usr/bin/env python3

def uppercase(str):
    texto = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            texto += chr(ord(c) - 32)
        else:
            texto += c
    print("{}".format(texto))
