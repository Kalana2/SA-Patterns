from abc import ABC, abstractmethod


# interface
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


# concrete implementations
class Truck(Transport):
    def deliver(self) -> str:
        return "Delivering by truck"


class Ship(Transport):
    def deliver(self) -> str:
        return "Delivering by ship"


# factory method
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()  # transport = Truck() or Ship()
        return transport.deliver()  # Truck().deliver() or Ship().deliver()


# concrete factories
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


# client code
def client_code(logistics: Logistics) -> None:
    print(logistics.plan_delivery())


if __name__ == "__main__":
    print("App: Launched with RoadLogistics.")
    client_code(RoadLogistics())

    print("\nApp: Launched with SeaLogistics.")
    client_code(SeaLogistics())


#  Output:
# App: Launched with RoadLogistics.
# Delivering by truck
# App: Launched with SeaLogistics.
# Delivering by ship


# Related patterns: Abstract Factory, Builder, Prototype, Singleton
