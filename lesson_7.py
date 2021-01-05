#task_1
from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"incompatible object type")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Matrix sizes difference")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2], [3, 4]])
    print(matrix1, '\n')

    matrix2 = Matrix([[10, 20], [30, 40]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)


#task_2
from abc import ABC, abstractmethod

from typing import Any


class AbstractClothes(ABC):
    """ Интерфейс одежды """
    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        """ Общая размерность одежды """
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    """ Одежда """
    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        """ Расход ткани """
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:
        """ Узнать размер """
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        """ Установить новый размер пальто """
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        """ Ткани на всю одежду """
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    """ Пальтишко """
    def _calc_tissue_required(self):
        """ посчитать расход ткани для пальто """
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        """ Узнать размер пальто """
        return self.measuring

    @V.setter
    def V(self, size: Any):
        """ Установить новый размер пальто """
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):
    """ Костюмчик """
    def _calc_tissue_required(self):
        """ посчитать расход ткани для костюма """
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        """ Узнать размер костюма """
        return self.measuring

    @H.setter
    def H(self, height: Any):
        """ Установить новый размер костюма """
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat('Пальто от Шанель', 5)
    print(coat)
    coat.V = 10
    print(coat)

    suit = Suit('Костюм от Бордо', 178)
    print(suit)
    suit.H = 200
    print(suit)

    print(coat.total_tissue_required)
    print(suit.total_tissue_required)


#task_3
class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)

        # raise ValueError(f"{self._count} - {other._count}: impossible operation")
        print(f"{self._count} - {other._count}: impossible operation")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


if __name__ == '__main__':
    c1 = Cell(17)
    print(c1)
    c2 = Cell(13)
    print(c2)

    print(c1 + c2)
    print(c1 - c2)
    print(c2 - c1)
    print(c2 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print((c1 * c2).make_order(23))
