from random import randint, choice

######################################################################################################################3
# Сортировка подсчетом
#
#
# Алгоритм
# Подсчитываем, сколько раз в массиве встречается каждое значение,
# и заполняем массив подсчитанными элементами в соответствующих количествах.
# Счётчики для всего диапазона чисел создаются заранее (изначально равны нулю).
#
#
# Сложность сортировки по времени
# 1.Худшая O(n + k)
# 2.Средняя O(n + k)
# 3.Лучшая O(n)
# Сложность сортировки по памяти
# O(M)
# M = колличество различных элементов
# Она не требует запоминания всех чисел в потоке данных
######################################################################################################################3


# формируем несортированный список
N = 5
a = []
for i in range(N):
    a.append(randint(0, 99))
print(a)

def counti(arr):
    scope = max(arr) + 1
    C = [0] * scope# создаем список из 10 нулей для подсчета чисел (от 0 до 9)
    for i in arr:  # Проходимся по нашему списку, считая какие цифры есть и сколько их.
        # т.е.[i] это индекс нашего списка из 10 нулей.
        C[i] += 1  # к каждому соответствующему индексу ставим +1
    return arr

def counting_sort(arr):
    scope = max(arr) + 1 #колличество счетчиков =  значение максимального элемента + 1 это делается для того чтобы мы могли обратиться к элементу котороый лежит в max()
    C = [0] * scope # создаем счетчики(список из scope(значение максимального элемента + 1) нулей) для подсчета чисел)
    for i in arr: # проходимся по нашему списку
        C[i] += 1 # и считаем какие цифры есть и сколько их
    arr[:] = [] # обнуляем наш список
    for number in range(scope):
        arr += [number] * C[number] # сохраняем в массив элемент [number] который равняется колличеству вхождений в массив
    return arr # возвращаем наш массив
print(counting_sort(a))