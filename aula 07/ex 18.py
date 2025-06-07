"""Crie uma função chamada strip_custom que aceita uma string e caracteres de remoção como argumentos e retorna uma nova string com os caracteres de remoção removidos dos extremos da string. Ela deve ter o mesmo comportamento que o método str.strip()."""

def strip_custom(texto: str, caracteres: str = " ") -> str:
    newTexto = ""
    for letra in texto:
        count = 0
        for carac in caracteres:
            if letra == carac:
                count += 1
        if count == 0:
            newTexto += letra
    return newTexto

texto = ">>>>Exemplo<<<"
print(texto.strip("<>"))
print(strip_custom(texto, "<>"))