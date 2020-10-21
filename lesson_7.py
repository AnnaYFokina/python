
#2------------------------------------------------------
from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_square_coat(self):
        return self.v / 6.5 + 0.5

    def get_square_suit(self):
        return self.h * 2 + 0.3

    @property
    def get_square_total(self):
        return str(f'Общая площадь ткани {round(((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)), 2)}')


class Coat(Cloth):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_coat = round((self.v / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Площадь на пальто {self.square_coat}'


class Suit(Cloth):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_suit = round((self.h * 2 + 0.3), 2)

    def __str__(self):
        return f'Площадь на костюм {self.square_suit}'

coat = Coat(2, 5)
suit = Suit(4, 2)
print(coat)
print(suit)
print(coat.get_square_total)
print(suit.get_square_total)
print(suit.get_square_suit())
print(coat.get_square_coat())

#3---------------------------------------------------------
class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        return f'Результат операции {self.cell * "*"}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return int(self.cell - other.cell) if (self.cell - other.cell) > 0 else print('Операция вычитания невозможна')

    def __mul__(self, other):
        return Cell(int(self.cell * other.cell))

    def __floordiv__(self, other):
        return Cell(round(self.cell // other.cell))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cell / cells_in_row)):
            row += f'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.cell % cells_in_row)}'
        return row

cells_1 = Cell(33)
cells_2 = Cell(9)
print(cells_1)
print(cells_1 + cells_2)
print(cells_2 - cells_1)
print(cells_2.make_order(5))
print(cells_1.make_order(5))
print(cells_1 // cells_2)



#2_1----------------------------------
from abc import ABC, abstractmethod, abstractmethod


class Cloth(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod
    def get_square_coat(self):
        pass

    @abstractmethod
    def get_square_suit(self):
        pass

    @property
    def get_square_total(self):
        return str(f'Общая площадь ткани {round(((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)), 2)}')


class Coat(Cloth):
    def get_square_coat(self):
        return f'Площадь ткани на пальто {round((self.v / 6.5 + 0.5), 2)}'

    def get_square_suit(self):
        return f'Площадь ткани на костюм {round((self.h * 2 + 0.3), 2)}'

    def __str__(self):
        return f'{self.get_square_coat()}'

class Suit(Cloth):
    def get_square_suit(self):
        return f'Площадь ткани на костюм {round((self.h * 2 + 0.3), 2)}'

    def get_square_coat(self):
        return f'Площадь ткани на пальто {round((self.v / 6.5 + 0.5), 2)}'

    def __str__(self):
        return f'{self.get_square_suit()}'

coat = Coat(2, 5)
suit = Suit(4, 2)
print(coat)
print(suit)
print(coat.get_square_total)
print(suit.get_square_total)
print(suit.get_square_suit())
print(coat.get_square_coat())

#1--------------------------

class Matrix:
    def __init__(self, matrix_1, matrix_2):
        # self.matr = [list_1, list_2]
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def __add__(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.matrix_1)):

            for j in range(len(self.matrix_2[i])):
                matrix[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))



my_matrix = Matrix([[100, 200, 300], [10, 20, 30], [1, 2, 3]], [[4, 5, 6], [44, 55, 66],[444, 555, 666]])

print(my_matrix.__add__())
