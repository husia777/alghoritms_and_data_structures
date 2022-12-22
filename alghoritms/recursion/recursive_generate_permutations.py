
def find(number, prefix):
    """
    ищет number в prefix
    :param number: число
    :param prefix: список
    :return: True or False
    """
    for x in prefix:
        if x == number:
            return True
    return False
def generate_permutations(N: int, M: int = -1, prefix=None):
    """
    Функция генерирует перестановку N чисел в M позициях начиная с префиксом prefix
    :param N: число
    :param M:колличество позиций
    :param prefix:
    :return:
    """
    M = N if M == -1 else M  # По умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(3)