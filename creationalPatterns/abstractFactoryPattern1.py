from abc import ABC, abstractmethod


# Abstract products Interface
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# concrete products
class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering Windows Button"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Windows Checkbox"


class MacButton(Button):
    def render(self) -> str:
        return "Rendering Mac Button"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Mac Checkbox"


# Abstract Factory Interface
class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# client code
def client_code(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


if __name__ == "__main__":
    print("Client: Testing client code with the WindowsFactory:")
    client_code(WindowsFactory())

    print("\nClient: Testing the same client code with the MacFactory:")
    client_code(MacFactory())
