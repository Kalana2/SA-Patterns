from abc import ABC, abstractmethod


# command interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# receiver
class Light:
    def on(self) -> None:
        print("The light is on")

    def off(self) -> None:
        print("The light is off")


# concrete commands
class LightOnCommand(Command):
    def __init__(self, light: "Light"):
        self._light = light

    def execute(self) -> None:
        self._light.on()


class LightOffCommand(Command):
    def __init__(self, light: "Light"):
        self._light = light

    def execute(self) -> None:
        self._light.off()


# invoker
class RemoteControl:
    def __init__(self):
        self._command: Command | None = None

    def set_command(self, command: Command) -> None:
        self._command = command

    def press_button(self) -> None:
        if self._command:
            self._command.execute()


# client code
if __name__ == "__main__":
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    remote_control = RemoteControl()
    remote_control.set_command(light_on_command)
    remote_control.press_button()

    remote_control.set_command(light_off_command)
    remote_control.press_button()
