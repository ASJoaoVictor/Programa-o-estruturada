"""Defina uma função chamada potencia que calcula a potência de um número elevado a uma potência especificada. Forneça uma documentação que explique como usar a função e inclua exemplos de uso."""

def potencia(num:int, exp:int) -> int:
    """
    calcula a potência

    :param num: Um número inteiro para elevar a potência
    :type num: int
    :param exp: Expoente da potência
    :type exp: int
    :return: Resultado da potência
    :rtype: int

    Exemplos:
    >>> potência(2, 3)
    8
    >>> potencia(3, 2)
    9
    """
    resultado = num ** exp
    return resultado

print(potencia(2,3))
print(potencia(3,2))