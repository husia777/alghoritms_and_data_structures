def invert_array(A: list, n: int):
    """
    Обращение массива задом-наперед
    :param A: список
    :param n: индекс
    :return: возвращает перевернутый массив
    """
    for i in range(n // 2):
        A[i], A[n - 1 - i] = A[n - 1 - i], A[i]
    return A


print(invert_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
