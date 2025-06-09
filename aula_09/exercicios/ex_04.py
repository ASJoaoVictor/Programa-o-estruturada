"""Dada uma lista de números, utilize map() com uma função lambda para criar uma nova lista 
onde cada número é multiplicado por 2, mas apenas se for maior que 5

Crie uma lista de quadrados dos números de 1 a 10 usando list comprehension.
Utilize a função map e uma função lambda para multiplicar por 2 os números maiores que 5"""

def dobro(n):
    if n > 5:
        return n*2
    return n

lista = [x**2 for x in range(1, 11)]
nova_lista = list(map(lambda n: n*2 if n > 5 else n, lista))

print(nova_lista)
