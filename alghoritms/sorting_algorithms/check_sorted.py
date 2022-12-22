def check_sorted(arr, asceting=True):
    """
    Функция проверяющая отсортирован ли массив за O(len(arr))
    :param arr: Массив
    :param asceting:
    :return: True/False
    """
    flag = True
    s = (2 * int(asceting))-1
    for i in range(0, len(arr)-1):
        if s * arr[i] > s * arr[i + 1]:
            flag = False
            break
    return flag