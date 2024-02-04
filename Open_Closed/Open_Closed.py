from abc import ABC, abstractmethod



class Shape(ABC):
    
    @abstractmethod
    def calculate_shape_area(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        super().__init__()
    
    def calculate_shape_area(self):
        return self.width * self.height


class Square(Shape):

    def __init__(self, side: int) -> None:
        self.side = side
        super().__init__()
    
    def calculate_shape_area(self):
        return self.side * self.side


class FindSize:

    def __init__(self, shape: Shape) -> None:
        self.shape = shape
    
    def find_area(self):
        return self.shape.calculate_shape_area()




square = Square(8)
rectangle = Rectangle(8, 9)

rectangle_area = FindSize(rectangle)
square_area = FindSize(square)

print(rectangle_area.find_area())
print(square_area.find_area())
