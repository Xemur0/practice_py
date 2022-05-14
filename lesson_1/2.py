# Реализовать функцию print_directory_contents(path).
# Функция принимает имя директории и выводит ее содержимое,
# включая содержимое всех поддиректории (рекурсивно вызывая саму себя).
# Использовать os.walk нельзя, но можно использовать
# os.listdir и os.path.isfile
import os
from pprint import pprint


def print_directory_contents(path):
    def get_directory_files(path):
        list_files = []
        for file_or_directory in os.listdir(path):
            full_name = os.path.join(os.path.abspath(path), file_or_directory)
            if os.path.isfile(full_name):
                list_files.append((os.path.abspath(path), file_or_directory))
            else:
                list_files.extend(get_directory_files(full_name))
        return list_files
    return get_directory_files(path)


pprint(print_directory_contents('./'))
