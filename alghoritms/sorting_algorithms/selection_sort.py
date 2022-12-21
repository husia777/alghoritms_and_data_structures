from random import randint

# Cортировка выбором
# формируем несортированный список
N = 5
a = []
for i in range(N):
    a.append(randint(0, 99))
print(a)


def selection_sort(l):
    "Алгоритм сортировки выбором с ипользованием for"
    for i in range(len(l)):
        max_el = max(l[0:len(l) - i])
        l[l.index(max_el)], l[-(i + 1)] = l[-(i + 1)], l[l.index(max_el)]
    return l


def selection_sort_by_while(l):
    "Алгоритм сортировки выбором с ипользованием while"
    n = len(l)
    while n > 0:
        l[l.index(max(l[0:n]))], l[n - 1] = l[n - 1], l[l.index(max(l[0:n]))]
        n -= 1
    return l

print(selection_sort(a))
print(selection_sort_by_while(a))
