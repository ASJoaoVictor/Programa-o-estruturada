"""Crie uma função chamada replace_custom que aceita uma string, uma substring antiga e uma 
substring nova como argumentos e retorna uma nova string com todas as ocorrências da substring 
antiga substituídas pela substring nova. Ela deve ter o mesmo comportamento que o método 
str.replace()."""

def replace_custom(texto: str, antigo: str,novo: str):
    novo_texto = ""
    for i in range(0, len(texto)):
        if (texto[i:i + len(novo)].endswith(antigo) or texto[i:i + len(novo)].startswith(antigo)):
            novo_texto += novo
            i += len(novo)
        else:
            novo_texto += texto[i]

        if len(texto) == i:
            break
    return novo_texto


texto = "O céu é azul. Azul é minha cor favorita."

print(texto.replace("azul", "verde"))
print(replace_custom(texto, "azul", "verde"))