"""Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!"."""

def saudacao(nome:str):
    print(f"Olá, {nome}")

nome = input("Digite seu nome: ")
saudacao(nome)