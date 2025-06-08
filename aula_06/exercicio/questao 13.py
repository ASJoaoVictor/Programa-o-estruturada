"""Exercício 13: Utilize a função enumerate() e um loop "for" para imprimir os elementos da lista numeros abaixo, juntamente com seus índices."""

frutas = ['maçã', 'banana', 'laranja', 'uva']

for indice, fruta in enumerate(frutas):
    print(f"indice: {indice} --> {fruta}")