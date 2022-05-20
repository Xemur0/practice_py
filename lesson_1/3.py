# Разработать целочисленный генератор случайных чисел.
# В функцию передавать начальную и конечную границу диапазона генерации
# (выдавать значения из диапазона включая концы).
# Заполнить этими данными словарь.
# Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”,
# а значене сгенеренное случайное число.  Вывести содержимое словаря.
# (Усложненный вариант по желанию*):
# Не использовать стандартный модуль python random.

import random
from pprint import pprint


def random_dict(start, finish):
    result = {}
    for i in range(start, finish + 1):
        random_int = int((finish - start) * random.random() + start)
        result.update({f'elem_{i}': random_int})
    return result


pprint(random_dict(1, 20), sort_dicts=False)
