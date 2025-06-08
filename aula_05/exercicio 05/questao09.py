#Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC).
#  Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

print(f"IMC: {imc}", end="---")

if(imc < 19.1):
    print("Abaixo do peso")
elif(imc < 25.8):
    print("Peso normal")
elif(imc < 27.3):
    print("Pouco acima do Peso")
elif(imc < 32.3):
    print("Acima do peso")
else:
    print("Obesidade")