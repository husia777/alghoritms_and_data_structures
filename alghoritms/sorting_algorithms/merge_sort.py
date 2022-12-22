from random import randint

######################################################################################################################3
# Сортировка слиянием
# Этот алгоритм относится к алгоритмам «разделяй и властвуй».
# Он разбивает список на две части, каждую из них он разбивает ещё на две и т. д.
# Список разбивается пополам, пока не останутся единичные элементы.

# Соседние элементы становятся отсортированными парами.
# Затем эти пары объединяются и сортируются с другими парами.
# Этот процесс продолжается до тех пор, пока не отсортируются все элементы.

# Алгоритм
# Список рекурсивно разделяется пополам, пока в итоге не получатся списки размером в один элемент.
# Массив из одного элемента считается упорядоченным.
# Соседние элементы сравниваются и соединяются вместе.
# Это происходит до тех пор, пока не получится полный отсортированный список.

# Сортировка осуществляется путём сравнения наименьших элементов каждого подмассива.
# Первые элементы каждого подмассива сравниваются первыми.
# Наименьший элемент перемещается в результирующий массив.
# Счётчики результирующего массива и подмассива, откуда был взят элемент, увеличиваются на 1.


######################################################################################################################3
# формируем несортированный список
N = 5
a = []
for i in range(N):
    a.append(randint(0, 99))
print(a)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0 #инициализируем начальные индексы для обоих массивов

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length): # проходимся по общей длине обоих списков:
        if left_list_index < left_list_length and right_list_index < right_list_length:# пока мы не дошли до конца в обоих списках
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)




# Проверяем, что оно работает
print(merge_sort(a))
