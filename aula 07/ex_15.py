"""Crie uma função chamada startswith_custom que aceita uma string e um prefixo como argumentos e retorna True se a string começar com o prefixo, caso contrário, retorna False. Ela deve ter o mesmo comportamento que o método str.startswith()."""

def startswith_custom(text: str, start: str) -> bool:
    if(text[0: len(start)] == start):
        return True
    else: 
        return False

print(startswith_custom("isso é legal", "isso"))