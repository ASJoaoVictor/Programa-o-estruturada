"""Escreva uma função em Python function que aceita uma string e 
retorna a quantidade de letras maiúsculas e minúsculas.
"""

def semNome(frase: str) -> int:
    maiuscula = minuscula = 0
    frase = frase.replace(" ", "")
    for letra in frase:
        if(letra.isupper()):
            maiuscula += 1
        else:
            minuscula += 1
    return maiuscula, minuscula

print(semNome("Hoje está um Dia Lindo para caminhar no parque"))
