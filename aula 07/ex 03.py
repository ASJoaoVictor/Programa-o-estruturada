"""Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. O idioma é opcional e padrão para "inglês". 
A função deve retornar uma saudação no idioma especificado."""

def saudacao_personalizada(nome:str, idioma = "pt-br"):
    match(idioma):
        case "pt-br":
            print(f"Olá, {nome}, como vai?")
        case "en":
            print(f"Hello, {nome}, how are you?")
        case "es":
            print(f"¡Hola, {nome}, ¿cómo estás?")
        case "fr":
            print(f"Bonjour, {nome}, comment ça va ?")

saudacao_personalizada("luiza")
saudacao_personalizada("luiza", "en")
saudacao_personalizada("luiza", "es")
saudacao_personalizada("luiza", "fr")
