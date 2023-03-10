######################################################################################################################3
#Ханойская башня
# Это математическая головоломка, в которой мы используем три одинаковых стержня и n дисков,
# все разных размеров. Диски расположены в первом стержне таким образом,
# что самый большой диск находится внизу, а самый маленький – вверху.
# Чтобы решить головоломку, нужно расположить диск в том же порядке в последнем стержне через средний стержень.
# Правила Ханойской башни на Python:
# Мы можем перемещать только один диск в любой момент времени
# Только диск, который находится наверху, может быть перемещен и помещен сверху на любой другой стержень
# Диск может быть помещен только поверх большего диска
######################################################################################################################3

def tower_of_hanoi(numbers, start, auxiliary, end):
    if(numbers):
        print('Move disk 1 from rod {} to rod {}'.format(start, end))
        return
    tower_of_hanoi(numbers - 1, start, end, auxiliary)
    print('Move disk {} from rod {} to rod {}'.format(numbers, start, end))
    tower_of_hanoi(numbers - 1, auxiliary, start, end)

tower_of_hanoi(2, 'A', 'B', 'C')

# Объяснение:
# 1)Здесь мы использовали рекурсивный метод для реализации игры
# 2)Функция Tower Of Hanoi() принимает четыре параметра:
# Количество дисков, Исходный стержень, Вспомогательный стержень, Конечный стержень,
# 3)Количество дисков
# 4)Источник стержень
# 5)Вспомогательный стержень
# 6)Стержень назначения
# 7)Он сначала проверяет условие, если номер диска равен 1, он непосредственно
# перемещает его к целевому стержню и завершает функцию
# 8)Затем мы рекурсивно вызвали функцию для перемещения оставшихся n-1 дисков из исходного узла во вспомогательный узел, используя стержень назначения в качестве вспомогательного
# 9)После этого оставшийся диск 1 непосредственно перемещается от исходного стержня к вспомогательному стержню
# 10)Наконец, мы снова рекурсивно вызвали функцию the для перемещения оставшихся n-1 стержней от вспомогательного стержня к целевому стержню, используя исходный узел в качестве вспомогательного