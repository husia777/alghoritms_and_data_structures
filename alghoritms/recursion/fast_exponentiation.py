def fast_exponention(a, n):
    """
    Алгоритм быстрого возведения в степень
    :param a: число которое нужно преобразовать
    :param n: степень в которую нужно возвести
    :return: a ** n
    """
    if n == 0:
        return 1
    elif n % 2 == 1:
        return fast_exponention(a, n - 1) * a
    else:
        return fast_exponention(a ** 2, n // 2)


print(fast_exponention(3, 3))
