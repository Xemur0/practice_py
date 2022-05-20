# Вывести таблицу умножения в виде:
# 1 x 1 = 1
# 1 x 2 = 2
# ..
# 1 x 10 = 10
# —
# 2 x 1 = 2
# 2 x 2 = 4
# …
# N x 10 = 10N
# Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
# Между разделами вывести разделитель в виде 5 девисов


def multiplication_table():
    try:
        from_multi = int(input('Введите число: '))
    except ValueError:
        return print('Нужно ввести число!'), multiplication_table()
    for i in range(from_multi, 11):
        for a in range(1, 11):
            print(f'{i} x {a} = {i * a}')
        print('-----')


multiplication_table()
