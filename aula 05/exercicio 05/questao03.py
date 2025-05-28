#Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
operacao = input("Escolha uma operação(+, -, *, /): ")

resultado:float

match operacao:
    case "+":
        resultado = num1 + num2
        print(f"{num1} {operacao} {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"{num1} {operacao} {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"{num1} {operacao} {num2} = {resultado}")
    case "/":
        resultado = num1 / num2
        print(f"{num1} {operacao} {num2} = {resultado}")
    case _:
        print("Operaçao invalída")