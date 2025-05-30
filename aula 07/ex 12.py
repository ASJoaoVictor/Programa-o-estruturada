"""Crie uma função chamada sum_custom que aceita uma lista de números como argumento e retorna a soma de todos os números na lista. Ela deve ter o mesmo comportamento que a função embutida sum()."""

def sum_custom(lista:list = []) -> int:
    soma = 0
    for n in lista:
        soma += n
    return soma

print(sum_custom([]))