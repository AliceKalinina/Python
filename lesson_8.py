#task_1
from typing import List, Tuple, Union
from math import floor


class Number(int):
    def __str__(self):
        return f"{self:02}"
#         :param date: кортеж (dd, mm, yyyy)
#         :return: bool оезультат проверки
#             # неверное число элементов в кортеже
#             # при распаковке приведет к ValueError
#
#         # метод статический, может быть вызван на любом наборе данных


class Date:
    date_attrs = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        fragments = date.split('-')

        if not self.validate(*fragments):
            raise ValueError(f"{date} invalid date format")

        self.day, self.month, self.year = self.transform(fragments)

    def __iter__(self):
        for attr in self.date_attrs:
            yield self.__getattribute__(attr)

    @classmethod
    def transform(cls, date: Union[List[str], Tuple[str]]) -> List[Number]:
        """ Приведение свалидированных элементов date к типу Number
        :param date: итерируемый объект с набором данных, готовых к преобразованию к типу Number
        :return:
        """
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date: Union[List[str], Tuple[str]]) -> bool:
        """ Валидация входных данных на формат и контент
        входные данные представляют дату в виде кортежа
        (dd, mm, yyyy).
        День считается валидным, если лежит в диапазоне 1 - 31.
        Месяц считается валидным, если лежит в диапазоне 1 - 12.
        Год считается валидным начиная с 1970
        :param date: кортеж с 3 элементами в парядке dd, mm, yyyy
        :return: True - если проверка на формат и контент пройдены, иначе - False
        """
        try:
            day, month, year = [int(x) for x in date]
        except TypeError:  # исключение как при распаковке. так и при приведениее
            return False

        bis_sextus = bool(not (year % 400 and year % 4) and year % 100)
        end_mon_day = 28 + (month + floor(month / 8)) % 2 + 2 % month + 2 * floor(1 / month)
        end_mon_day += bis_sextus if month == 2 else 0

        return all([1 <= day <= end_mon_day, 1 <= month <= 12, year >= 1970])

    def __str__(self):
        return f"Date is '{'-'.join([str(s) for s in self])}'"


if __name__ == '__main__':
    for date in ('01-12-2011', '01-12-1969', '29-02-2020', '29-02-2021'):
        try:
            print(Date(date))
        except ValueError as e:
            print(e)
            
            
            
    #task_2
    class MyZeroDivisionError(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
            print(dividend / divider)
        except MyZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
            break




#task_3
class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []

    while True:
        user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")

        if user_input == "stop":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' has not numerical format")

            my_list.append(int(user_input))
        except NotNumberError as e:
            print(e)

    print(my_list)



task_4

class Storage:
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color

        self.purchase_price = purchase_price

        self.printable = True if self.type in ("printer", "xerox") else False
        self.scannable = True if self.type in ("scanner", "xerox") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('xerox', *args)


if __name__ == '__main__':
    p1 = Printer("Epson", "XP-400", "white", 4000)
    print(p1)




#task_5
class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} не оргтехника")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('xerox', *args)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("Epson", "XP-400"))
    storage.add(Scanner("OKI", "5367-AD"))
    storage.add(Xerox("Xerox", "F123"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("Передаем 1 устройство")
    storage.transfer(last_idx, 'Отдел ЯФ')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print("Удаляем 1 устройство")
    del storage[last_idx]
    print(storage)





#task_6
class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStorageError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddStorageError = AcceptStorageError


class ValidateEquipmentError(AppError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorageError(f"Вы пытаетесь добавить на склад не оргтехнику")

        self.__storage.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer.create(4, vendor="Epson", model="XP-400"))
    storage.add(Scanner.create(3, vendor="OKI", model="5367-AD"))
    storage.add(Scanner.create(2, vendor="OKI", model="5368-AD"))
    storage.add(Xerox.create(6, vendor="Xerox", model="F123"))
    print(storage)

    for idx, itm in storage.filter_by(department=None, vendor="OKI", model="5367-AD"):
        print(f"Резервируем {itm} в 'Отдел ЯФ'")
        storage.transfer(idx, 'Отдел ЯФ')

    for idx, itm in storage.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print(storage)
    print("Списываем 1 устройство")
    del storage[0]
    print(storage)




#task_7
class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = MyComplex(2, -3)
    c2 = MyComplex(5)

    print(c1 + c2, complex(2, -3) + complex(5))
    print(c1 * c2, complex(2, -3) * complex(5))

