from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, brand: str, model: str, issue_year: int, color: str):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0

    @abstractmethod
    def move(self, num_km: int) -> str:
        if num_km <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self.mileage += num_km

class Car(Transport):
    def __init__(self, brand: str, model: str, issue_year: int, color: str, engine_type: str):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, num_km: int) -> str:
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {num_km} километров"

class Airplane(Transport):
    def __init__(self, brand: str, model: str, issue_year: int, color: str, lifting_capacity: int):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, num_km: int) -> str:
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) пролетел {num_km} километров"


car = Car("Citroen", "C5", 2004, "Зеленый", "Бензиновый")
airplane = Airplane("Boeing", "747", 2015, "Белый", 80000)


print(car.move(100))
print(airplane.move(500))

try:
    car.move(-50)
except ValueError as e:
    print(e)