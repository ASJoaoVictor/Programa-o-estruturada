"""Crie uma função chamada split_custom que aceita uma string e um caractere de separação como argumentos e retorna uma lista de substrings separadas pelo caractere de separação. Ela deve ter o mesmo comportamento que o método str.split()."""

def split_custom(texto: str, carac: str = " ") -> list:
    newtexto = []
    palavra = ""
    for i, letra in enumerate(texto):
        if letra == carac:
            newtexto.append(palavra)
            palavra = ""
        elif i == len(texto) - 1:
            palavra += letra
            newtexto.append(palavra)
        else:
            palavra += letra
    return newtexto

frase = "isso é um palavra da função split"

print(frase.split())
print(split_custom(frase))