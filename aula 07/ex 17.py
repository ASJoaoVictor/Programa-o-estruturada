"""Crie uma função chamada split_custom que aceita uma string e um caractere de separação como argumentos e retorna uma lista de substrings separadas pelo caractere de separação. Ela deve ter o mesmo comportamento que o método str.split()."""

def split_custom(text: str, carac: str = " ") -> list:
    newText = []
    teste = ""
    for i in text:
        if i != carac or i == text[-1]:
            teste += i
        else:
            newText.append(teste)
            teste = ""
    return newText

frase = "isso é um teste da função split"

print(frase.split("s"))
print(split_custom(frase, "s"))