from abc import ABC, abstractmethod


# Abstract Factory Interface
class Furniture(ABC):
    @abstractmethod
    def create_chair(self) -> str:
        pass

    @abstractmethod
    def create_sofa(self) -> str:
        pass

    @abstractmethod
    def create_table(self) -> str:
        pass


# Concrete Factories
class VictorianFurniture(Furniture):
    def create_chair(self) -> str:
        return "Victorian Chair"

    def create_sofa(self) -> str:
        return "Victorian Sofa"

    def create_table(self) -> str:
        return "Victorian Table"


class ModernFurniture(Furniture):
    def create_chair(self) -> str:
        return "Modern Chair"

    def create_sofa(self) -> str:
        return "Modern Sofa"

    def create_table(self) -> str:
        return "Modern Table"


class ArtDecoFurniture(Furniture):
    def create_chair(self) -> str:
        return "Art Deco Chair"

    def create_sofa(self) -> str:
        return "Art Deco Sofa"

    def create_table(self) -> str:
        return "Art Deco Table"


# concrete products
class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> str:
        pass


class VictorianChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a Victorian Chair"


class ModernChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a Modern Chair"


class ArtDecoChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on an Art Deco Chair"


class Sofa(ABC):
    @abstractmethod
    def lie_on(self) -> str:
        pass


class VictorianSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a Victorian Sofa"


class ModernSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a Modern Sofa"


class ArtDecoSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on an Art Deco Sofa"


class Table(ABC):

    @abstractmethod
    def dine_on(self) -> str:
        pass


class VictorianTable(Table):
    def dine_on(self) -> str:
        return "Dining on a Victorian Table"


class ModernTable(Table):
    def dine_on(self) -> str:
        return "Dining on a Modern Table"


class ArtDecoTable(Table):
    def dine_on(self) -> str:
        return "Dining on an Art Deco Table"


if __name__ == "__main__":
    for factory in (VictorianFurniture(), ModernFurniture(), ArtDecoFurniture()):
        chair = factory.create_chair()
        sofa = factory.create_sofa()
        table = factory.create_table()
        print(f"{chair}, {sofa}, {table}")
