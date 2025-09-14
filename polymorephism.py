from abc import ABC, abstractmethod


class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(AbstractAnimal):
    def speak(self):
        return "Woof!"


class Cat(AbstractAnimal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.speak())  # Outputs: Woof!
print(cat.speak())  # Outputs: Meow!
