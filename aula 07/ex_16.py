"""Crie uma função chamada endswith_custom que aceita uma string e um sufixo como argumentos e retorna True se a string terminar com o sufixo, caso contrário, retorna False. Ela deve ter o mesmo comportamento que o método str.endswith()."""

def endswith_custom(text: str, end: str) -> bool:
    if(text[len(text) - len(end):] == end):
        return True
    else:
        return False
    
print(endswith_custom("isso é legal", "legal"))