# the wrong way
class Animals:
    def __init__(self) -> None:
        super().__init__()
    
    def eat(self):
        return super().eat()
    
    def walk(self):
        return super().walk()
    
    def fly(self):
        # not all the animals can fly
        pass


# the right way
class Animals:
    def __init__(self) -> None:
        pass
    
    def eat(self):
        pass
    
    def walk(self):
        pass


class FliableAnimals(Animals):
    def __init__(self) -> None:
        super().__init__()
    
    def eat(self):
        return super().eat()
    
    def walk(self):
        return super().walk()
    
    def fly(self):
        pass
