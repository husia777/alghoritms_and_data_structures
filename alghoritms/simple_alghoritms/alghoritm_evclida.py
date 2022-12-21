def algorithm_eklida(a, b):
    if b == 0:
        return a
    return algorithm_eklida(a, b % a)


print(algorithm_eklida(8, 16))