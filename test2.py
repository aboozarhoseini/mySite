class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        return super().area() * 10


class Cube(Square):

    def area(self):
        return super(Square, self).area()


sq = Square(10)
print(sq.area())
print(sq.perimeter())

print('-----------------')

cu = Cube(10)

print(cu.area())
print(cu.perimeter())

print(isinstance(sq, Square))

print('fffffffffffffffffffffffffffffffffff')
