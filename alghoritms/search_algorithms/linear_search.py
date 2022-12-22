###############################################################################################################################################################
# Алгоритмы сортировки нужны, чтобы быстрее потом искать элементы в этом массиве!!!!!
###############################################################################################################################################################
# Временная сложность линейного поиска: O(n).

# Линейный поиск нечасто используется на практике,
# однако хорошо подходит для тех случаев,
# когда нам нужно найти первое вхождение элемента в несортированной коллекции.
# Это связано с тем, что он не требует сортировки коллекции перед поиском
# (в отличие от большинства других алгоритмов поиска).
###############################################################################################################################################################
def LinearSearch(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1
