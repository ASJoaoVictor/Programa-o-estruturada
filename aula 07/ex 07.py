"""7 Implemente uma função validar_email que verifica se uma string fornecida como argumento representa um endereço de e-mail válido. Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com"""

def verificar_email(email:str) -> bool:
    """
    Verificar se o email é válido

    :param email: É o email
    :type email: str
    :return: True se o e-mail for válido, False caso contrário.
    :rtype: boolean

    Exemplos:
    >>> verificar_email("Luiza@gmail.com")
    True
    >>> verificar_email("vanessa@outloocom")
    False
    >>> verificar_email("pedrogmail.com")
    False
    >>> verificar_email("vini dantas@gmail.com")
    False
    """
    if(" " not in email and email.count("@") == 1 and email[-4:] == ".com"):
        return True
    else:
        return False
    
print(verificar_email("teste@g@mail.com"))