def generate_numbers(N: int, M: int, prefix=None):
    """
    Функция которая генерирует все числа (с лидирующими незначащими нулями) N-ричной системе счисления
    N<=10 длины M
    :param N:основание системы счисления
    :param M:кол-во чисел
    :return:
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

print(generate_numbers(10, 5))