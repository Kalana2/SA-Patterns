from abc import abstractmethod, ABC


# Product
class Computer:
    def __init__(self):
        self.cpu: str | None = None
        self.ram: str | None = None
        self.storage: str | None = None
        self.gpu: str | None = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage}, gpu={self.gpu})"


# Builder Interface
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu: str) -> "ComputerBuilder":
        pass

    @abstractmethod
    def set_ram(self, ram: str) -> "ComputerBuilder":
        pass

    @abstractmethod
    def set_storage(self, storage: str) -> "ComputerBuilder":
        pass

    @abstractmethod
    def set_gpu(self, gpu: str) -> "ComputerBuilder":
        pass

    @abstractmethod
    def build(self) -> Computer:
        pass


# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram: str):
        self.computer.ram = ram
        return self

    def set_gpu(self, gpu: str):
        self.computer.gpu = gpu
        return self

    def set_storage(self, storage: str):
        self.computer.storage = storage
        return self

    def build(self) -> Computer:
        return self.computer


class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram: str):
        self.computer.ram = ram
        return self

    def set_storage(self, storage: str):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu: str):
        self.computer.gpu = gpu
        return self

    def build(self) -> Computer:
        return self.computer


# Director
class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_gaming_computer(self) -> Computer:
        return (
            self.builder.set_cpu("Intel i9")
            .set_ram("32GB")
            .set_storage("1TB SSD")
            .set_gpu("NVIDIA RTX 3080")
            .build()
        )

    def construct_office_computer(self) -> Computer:
        return (
            self.builder.set_cpu("Intel i5")
            .set_ram("16GB")
            .set_storage("512GB SSD")
            .set_gpu("Integrated Graphics")
            .build()
        )


# Client Code
if __name__ == "__main__":
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    gaming_computer = director.construct_gaming_computer()
    print(gaming_computer)

    office_builder = OfficeComputerBuilder()
    director = ComputerDirector(office_builder)
    office_computer = director.construct_office_computer()
    print(office_computer)
