from abc import ABC, abstractmethod


class Shape(ABC):

    def area(self) -> int:
        pass


class Rectangle(Shape):
    
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def area(self) -> int:
        return self.width * self.height


class Square(Shape):

    def __init__(self, length: int) -> None:
        self.length = length
    
    def area(self) -> int:
        return self.length * self.length


square = Square(8)
rectangle = Rectangle(8, 9)

print(square.area())
print(rectangle.area())


# another solution

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, length: int) -> None:
        super().__init__(length, length)
    
    def area(self):
        return super().area()


square = Square(8)
rectangle = Rectangle(8, 9)

print(square.area())
print(rectangle.area())
