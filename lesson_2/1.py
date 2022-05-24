# Создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену.
# Второй — дочерний (ItemDiscountReport), должен содержать функцию
# (get_parent_data), отвечающую за отображение информации о товаре
# в одной строке вида (“{название товара} {цена товара}”).
# Создать экземпляры родительского класса и дочернего.
# Распечатать информацию о товаре.

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price



class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.name} - {self.price}'


item = ItemDiscount('TV', 10000)
discount = ItemDiscountReport(item.name, item.price)
print(discount.get_parent_data())


# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет
# сгенерирована ошибка выполнения. Усовершенствовать родительский класс
# таким образом, чтобы получить доступ к защищенным переменным. Результат
# выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.name} - {self.price}'


item = ItemDiscount('TV-2', 10000)
discount = ItemDiscountReport(item.name, item.price)
print(discount.get_parent_data())


#Реализовать возможность переустановки значения цены товара в
# родительском классе. Проверить, распечатать информацию о товаре.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.name} - {self.price}'


item = ItemDiscount('TV-3', 10000)
print(item.name, item.price)

item.name, item.price = 'TVTOPTOP', 10000000

item_discount_report = ItemDiscountReport(item.name, item.price)
print(item_discount_report.get_parent_data())

# Реализовать расчет цены товара со скидкой. Величина скидки должна
# передаваться в качестве аргумента в дочерний класс. Выполнить перегрузку
# методов конструктора дочернего класса (метод __init__, в который должна
# передаваться переменная — скидка), и перегрузку метода __str__ дочернего
# класса. В этом методе должна пересчитываться цена и возвращаться результат
# — цена товара со скидкой. Чтобы все работало корректно, не забудьте
# инициализировать дочерний и родительский классы (вторая и третья строка
# после объявления дочернего класса).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, percent=0):
        super().__init__(name, price)
        self.percent = percent

    def get_parent_data(self):
        return f'{self.name} - {self.price}'

    def __str__(self):
        sale = self.price - self.price * (self.percent / 100)
        return f'{self.name} - Цена со скидкой: {sale}'

item = ItemDiscount('TV-4', 10000)
discount = ItemDiscountReport(item.name, item.price, 99)
print(discount.get_parent_data())
print(str(discount))


# Проверить на практике возможности полиморфизма. Необходимо разделить
# дочерний класс ItemDiscountReport на два класса. Инициализировать классы
# необязательно. Внутри каждого поместить функцию get_info, которая в первом
# классе будет отвечать за вывод названия товара, а вторая — его цены. Далее
# реализовать вызов каждой из функции get_info.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val

    def __str__(self):
        return f'Name - {self.name} |  Price - {self.price}'


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, percent=0):
        super().__init__(name, price)
        self.percent = percent

    def get_parent_data(self):
        return f'{self.name} - {self.price}'

    def __str__(self):
        sale = self.price - self.price * (self.percent / 100)
        return f'{self.name} - Цена со скидкой: {sale}'


class ItemInfoName(ItemDiscount):

    def get_info(self):
        return f'Name - {self.name}'


class ItemInfoPrice(ItemDiscount):

    def get_info(self):
        return f'Price - {self.price}'


item = ItemDiscount('TV-1', 10000)
print(str(item))
name_item = ItemInfoName(item.name, item.price)
price_item = ItemInfoPrice(item.name, item.price)
print(ItemInfoName.get_info(name_item))
print(ItemInfoPrice.get_info(price_item))
