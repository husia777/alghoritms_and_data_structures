def cyclic_array_shift_left(A: list, n: int):
    """
    Циклический сдвиг массива влево
    :param A: список
    :param n: индекс
    :return: возвращает  массив элементы которого сдвинулись на 1 индекс влево
    """
    tmp = A[0]
    for i in range(n - 1):
        A[i] = A[i + 1]
    A[-1] = tmp
    return A


def cyclic_array_shift_right(A: list, n: int):
    """
    Циклический сдвиг массива влево
    :param A: список
    :param n: индекс
    :return: возвращает  массив элементы которого сдвинулись на 1 индекс вправо
    """
    tmp = A[n - 1]
    for i in range(n - 2, -1, -1):
        A[i + 1] = A[i]
    A[0] = tmp
    return A


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cyclic_array_shift_left(my_list, 11))

print(cyclic_array_shift_right([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
