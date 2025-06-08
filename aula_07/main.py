def saudacao(nome:str):
    print(f"Olá, {nome}")

def dobro(num:int) -> int:
    return num*2

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