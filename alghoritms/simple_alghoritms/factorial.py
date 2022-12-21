def factorial(n):
    """
    Функция которая вычисляет факториал числа
    :param n: факториал от какого числа нужно вычислить
    :return: факториал от n
    """
    if n == 0:
        return 1
    return factorial(n-1) * n

print(factorial(5))