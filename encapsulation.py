class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


p = Point()
p.x = 10
p.y = 20
print(p.x, p.y)  # Outputs: 10 20


class Salary:
    def __init__(self, pay, bonus):
        self.__pay = pay
        self.__bonus = bonus


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary


s = Salary(1000, 500)
e = Employee("John", s)
print(
    e._Employee__salary._Salary__pay
)  # Accessing private attribute using name mangling
