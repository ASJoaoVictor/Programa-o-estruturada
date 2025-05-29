"""Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150.

"""

def idade_valida(idade):
    """
    Verificar de idade é int e se está entre 0 a 150

    :param idade: O valor da idade
    :type idade: int
    :return: True se a idade for válida, False caso contrário
    :rtype: boolean

    Exemplos:
    >>> idade_valida(20)
    True

    >>> idade_valida(2.0)
    False
    """
    if(isinstance(idade, int) and 0 <= idade <= 150):
        return True
    else:
        return False
    
print(idade_valida(2))