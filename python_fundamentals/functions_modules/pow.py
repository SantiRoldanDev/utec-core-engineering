#!/usr/bin/env python3

def pow(a, b):
    contador = 0
    resultado = 1
    while contador < abs(b):
        resultado *= a
        contador += 1
    if b < 0:
        return 1 / resultado
    return resultado
