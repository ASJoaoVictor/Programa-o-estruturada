"""Crie uma função chamada max_custom que aceita uma lista de números como argumento e retorna o maior número na lista. Ela deve ter o mesmo comportamento que a função embutida max().

"""

def max_custom(lista: list) -> int:
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior

print(max_custom([1, 9, 8, 71, 2]))