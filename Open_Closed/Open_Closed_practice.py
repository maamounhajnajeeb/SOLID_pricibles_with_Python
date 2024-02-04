class Square:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Cube(Square):
    def __init__(self, width: int, height: int, length: int) -> None:
        self.length = length
        super().__init__(width, height)
    
    def size(self):
        return self.area() * self.length


square = Square(8, 9)
cube = Cube(8, 9, 10)

print(square.area())
print(cube.size())