#!/usr/bin/env python3

def pow(a, b):
    contador = 0
    resultado = 1
    while contador < b:
        resultado *= a
        contador += 1
    return resultado
