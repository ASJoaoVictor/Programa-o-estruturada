"""A função map é uma função que aceita uma outra função como argumento e um iterável (*args). Ela retorna uma lista de valores que passaram pela primeira função passada como argumento. 
Crie uma lista que formata todos os nomes passados para um valor em maiúsculo."""

def toUpper(string: str):
    return string.upper()

print(list(map(toUpper, "isso é apenas um teste")))