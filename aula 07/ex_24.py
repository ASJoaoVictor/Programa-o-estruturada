"""A função filter é uma função que aceita uma outra função como argumento e um iterável (*args). Ela filtra todos os valores que são False a partir da primeira função passada, retornando uma lista de valores que retornaram True. 
Crie um filtro que recebe uma lista de números e retorna os pares."""

def par(num):
    if num % 2 == 0:
        return True
    return False

def filtro(lista: list):
    return_lista = []
    for i in lista:
        if par(i):
            return_lista.append(i)
    return return_lista

print(filtro([1, 2, 4, 5, 6, 7, 8]))
print(list(filter(par, [1, 2, 4, 5, 6, 7, 8])))