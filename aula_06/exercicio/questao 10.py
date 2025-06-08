"""Exercício 10: Escreva um programa que peça ao usuário para digitar uma senha e continue pedindo até que o usuário digite a senha correta.
 Quando a senha estiver correta, imprima uma mensagem de boas-vindas."""

senhaCorreta = "senha"
acesso = False

while(not acesso):
    senha = input("Digite a senha: ")
    if(senhaCorreta == senha):
        print("Boas-vindas")
        break
    else:
        print("Senha incorreta")
