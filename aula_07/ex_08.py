"""Escreva uma função calcular_pagamento que aceita os parâmetros nomeados horas_trabalhadas e 
taxa_hora e retorna o pagamento total."""

def calcular_pagamento(horas_trabalhadas: float, taxa_hora: float) -> float:
    return horas_trabalhadas * taxa_hora

print("R",calcular_pagamento(40, 10))