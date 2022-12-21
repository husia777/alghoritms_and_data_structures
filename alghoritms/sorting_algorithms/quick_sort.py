from random import randint, choice

# Быстрая сортировка неоптимальный вариант
# формируем несортированный список
N = 5
a = []
for i in range(N):
    a.append(randint(0, 99))
print(a)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    avg = choice(arr)
    left = [i for i in arr if i < avg]
    right = [i for i in arr if i > avg]
    middle = [i for i in arr if i == avg]
    return quick_sort(left) + middle + quick_sort(right)


def optimal_quick_sort(arr, fst, lst):
    if fst >= lst: #если индекс начального элемента больше либо равен индексу конечного программа завершается(отсортировали все элементы)
        return
    i, j = fst, lst  # начальный и конечный элемент нашего списка
    pivot = arr[(fst + lst) // 2]    #  опорный элемент равен элементу находящемуся по середине
    while i <= j: # пока начальный индекс меньше либо равно конечному
        while a[i] < pivot: #если первый элемент  меньше опорного элемента
            i += 1 # берем следующий и так пока условие истинно
        while a[j] > pivot: #если последний элемент  больше опорного элемента
            j -= 1 #берем предыдущий и так пока условие истинно
        if i <= j: # если начальный индекс меньше либо равен конеченому
            a[i], a[j] = a[j], a[i] #меняем их местами
            i, j = i + 1, j - 1 # начальный индекс увеличиваем на 1 а конечный уменьшаем на 1
    optimal_quick_sort(arr, fst, j) #рекурсивно вызываем нашу функцию
    optimal_quick_sort(arr, i, lst) #


print(quick_sort(a))
optimal_quick_sort(a, 0, len(a) - 1)
print(a)
