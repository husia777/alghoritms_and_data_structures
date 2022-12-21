def resheto_eratosphena(n):
    """
    Простое число — такое натуральное число, которое имеет ровно 2 различных натуральных делителя:
     себя и единицу.

    Асимптотика этого алгоритма O(n log log n), то есть на практике O(n)

    Решето Эратосфена – это алгоритм нахождения простых чисел до заданного натурального числа
    путем постепенного отсеивания составных чисел.
    Образно говоря, через решето Эратосфена в процессе его тряски проскакивают составные числа,
     а простые остаются в решете.
    :return:
    """
    is_prime = [True] * (n + 1)  # Отметим все числа простыми
    is_prime[0], is_prime[1] = False, False  # Убираем 0 и 1 из простых
    for i in range(2, n + 1):  # пробегаемся по по нашим числам
        if is_prime[i]:  # если число простое
            for j in range(2 * i, n + 1, i):  # Убираем числа, которые делятся на i
                is_prime[j] = False
    primes = []  # Формируем список простых
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


def optimal_resheto_eratosphena(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):  # Заменили 2 * i на i ** 2
                is_prime[j] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


print(resheto_eratosphena(1000))
print(optimal_resheto_eratosphena(1000))
