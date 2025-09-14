from abc import ABC, abstractmethod


# Prototype Interface
class Shape(ABC):
    @abstractmethod
    def clone(self) -> "Shape":
        pass


# Concrete Prototype
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def clone(self) -> "Circle":
        return Circle(self.radius)

    def __str__(self):
        return f"Circle(radius={self.radius})"


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def clone(self) -> "Square":
        return Square(self.side)

    def __str__(self):
        return f"Square(side={self.side})"


# Client Code
def main():
    circle1 = Circle(5)
    circle2 = circle1.clone()
    print(circle1)  # Output: Circle(radius=5)
    print(circle2)  # Output: Circle(radius=5)

    square1 = Square(4)
    square2 = square1.clone()
    print(square1)  # Output: Square(side=4)
    print(square2)  # Output: Square(side=4)


if __name__ == "__main__":
    main()
