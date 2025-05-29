"""Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) 
e retorna a base elevada ao expoente."""

def potencia(base:int, exp = 2) -> int:
    return base ** exp

print(potencia(2))
print(potencia(2, 3))
print(potencia(3, 4)) 