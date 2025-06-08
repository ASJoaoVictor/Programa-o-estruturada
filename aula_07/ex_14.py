"""Crie uma função chamada min_custom que aceita uma lista de números como argumento e retorna o menor número na lista. Ela deve ter o mesmo comportamento que a função embutida min()."""

def min_custom(lista: list) -> int:
    menor = lista[0]
    for n in lista:
        if n < menor:
            menor = n
    return menor

print(min_custom([9, 0, 2, 1]))