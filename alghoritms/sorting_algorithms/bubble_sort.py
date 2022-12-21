from random import randint
from time import time
######################################################################################################################3
#Пузырьковая сортировка
# Этот простой алгоритм выполняет итерации по списку, сравнивая элементы попарно
# и меняя их местами, пока более крупные элементы не «всплывут» в начало списка,
# а более мелкие не останутся на «дне».
#Алгоритм
# Сначала сравниваются первые два элемента списка.
# Если первый элемент больше, они меняются местами.
# Если они уже в нужном порядке, оставляем их как есть.
# Затем переходим к следующей паре элементов, сравниваем их значения
# и меняем местами при необходимости.
# Этот процесс продолжается до последней пары элементов в списке.
# При достижении конца списка процесс повторяется заново для каждого элемента.
# Это крайне неэффективно, если в массиве нужно сделать, например, только один обмен.
# Алгоритм повторяется n² раз, даже если список уже отсортирован.

######################################################################################################################3

# формируем несортированный список
N = 5
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

for i in range(N - 1): #для сортировки массива длиной N надо N-1 итераций
    for j in range(N - 1 - i): #эта запись нужна для того чтобы после сортировки не рассматривать элементы которые находятся в конце
        if a[j] > a[j + 1]: #если текущий элемент больше следующего то
            a[j], a[j + 1] = a[j + 1], a[j] # меняем местами

print(a)

