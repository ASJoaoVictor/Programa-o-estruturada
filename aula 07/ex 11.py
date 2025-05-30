"""Crie uma função chamada len_custom que aceita um iterável (por exemplo, uma lista ou uma string) como argumento e retorna o número de elementos no iterável. Ela deve ter o mesmo comportamento que a função embutida len()."""

def len_custom(interavel) -> int:
    """
    Conta o número elementos de um iterável

    :param interavel: Objeto que será contado o número de elementos
    :type interavel: list ou str
    :return: número de elementos
    :rtype: int

    sample:
    >>> len_custom([1, 2, 4])
    3
    >>> len_custom("Good day")
    8
    """
    count = 0
    for i in interavel:
        count += 1
    return count

print(len_custom("good day"))