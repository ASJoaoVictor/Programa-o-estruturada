"""Crie uma função que aceita *args e retorna a soma de todos os números passados como 
argumentos."""

def soma(*args):
    total = 0
    for n in args:
        total += n
    return total

print(soma(1, 2, 4, 5))