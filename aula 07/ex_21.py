"""Escreva uma função que recebe *args e retorna o número de argumentos passados."""

def custom_len(*args):
    quant = 0
    for n in args:
        quant += 1
    return quant

print(custom_len(1, 2, 4, 1))