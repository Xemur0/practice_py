# Написать программу, которая будет содержать функцию для получения имени
# файла из полного пути до него. При вызове функции в качестве аргумента
# должно передаваться путь и имя файла с расширением. В функции необходимо
# реализовать поиск имени файла (с расширением), а затем «выделение» имени
# файла (без расширения). Расширений может быть несколько
# (например testfile.tar.gz).
from itertools import zip_longest
from os import path
from random import randint


def get_file_name(path):
    return path.split('/')[-1].split('.')[0]


print(get_file_name('/var/logs/nginx/error.tar.gz'))

# Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.


def parts_of_numbers():
    string = input('Введите число: ')
    try:
        number = float(string)
        if int(number) == number:
            return 'Целое'
        else:
            left, right = string.split('.')
            return left == right, 'дробное'
    except ValueError:
        print('Не число')


print(parts_of_numbers())


# Создать два списка с различным количеством элементов. В первом должны быть
# записаны ключи, во втором — значения. Необходимо написать функцию,
# создающую из данных ключей и значений словарь. Если ключу не хватает
# значения, в словаре для него должно сохраняться значение None. Если есть
# значения, которым не хватило ключей, их необходимо отбросить.


def get_dict(list_1, list_2):
    result = dict(zip_longest(list_1, list_2, fillvalue=None))
    filtered = dict(filter(lambda x: x[0] is not None, result.items()))
    return filtered


print(get_dict([1, 2, 3, 4], [10, 20, 30, 40, 50, 60, 70]))
print(get_dict([1, 2, 3, 4, 5, 6, 7, 8], [10, 20, 30, 40]))

# Написать программу, в которой реализовать две функции. В первой должен
# создаваться простой текстовый файл. Если файл с таким именем уже существует,
# выводим соответствующее сообщение и завершаем работу. Необходимо открыть
# файл и создать два списка: с текстовой и числовой информацией. Для создания
# списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен должен быть обработан и записан в
# файл таким образом, чтобы каждая строка файла содержала текстовое и числовое
# значение (например example345). Вызвать вторую функцию. В нее должна
# передаваться ссылка на созданный файл. Во второй функции необходимо
# реализовать открытие файла и простой, построчный вывод содержимого.


def create(file_name):
    if path.exists(file_name):
        return f'!{file_name}! is already exist'
    else:
        random_int = (str(randint(100, 1000)) for _ in range(10))
        text = ("example" for _ in range(10))
        res_zip = list(map(lambda x: ''.join(x) + '\n', zip(text, random_int)))
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(res_zip)
        return f'!{file_name}! is created'


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')


def find_text(file_name, text, find_all=True):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if text in line:
                print(line, end='')
            if not find_all:
                break


def replace_text(file_name, old_text, new_text):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if old_text in line:
                print(line.replace(old_text, new_text), end='')


create('test.txt')
read_file('test.txt')
print('*' * 15, 'Поиск со всеми вхождениями', '*' * 15)
find_text('test.txt', 'exam', True)
print('*' * 15, 'Поиск с первым вхождением', '*' * 15)
find_text('test.txt', 'exam', False)
print('*' * 15, 'Замена текста', '*' * 15)
replace_text('test.txt', 'example', 'la')
