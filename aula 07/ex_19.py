"""Crie uma função chamada replace_custom que aceita uma string, uma substring antiga e uma 
substring nova como argumentos e retorna uma nova string com todas as ocorrências da substring 
antiga substituídas pela substring nova. Ela deve ter o mesmo comportamento que o método 
str.replace()."""

def replace_custom(texto: str, antigo: str,novo: str):
    novo_texto = ""
    i = 0
    while True:
        if len(texto) == i:
            break
        elif (texto[i:i + len(antigo)] == antigo or texto[i:i + len(novo)] == antigo):
            novo_texto += novo
            i += len(antigo)
        else:
            novo_texto += texto[i]
            i += 1
    return novo_texto


texto = "O céu é azul. Azul é minha cor favorita."

print(texto.replace("azul", "rosa"))
print(replace_custom(texto, "azul", "rosa"))