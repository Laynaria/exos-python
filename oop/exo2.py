from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int):
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.speed: int = 0 # correction to initialize the speed always at 0 without being able to set a speed from a new vehicle

    # GETTERS / SETTERS

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, new_brand) -> None:
        self._brand = new_brand

    @property
    def model(self) -> str:
        return self._model
    
    @model.setter
    def model(self, new_model) -> None:
        self._model = new_model

    @property
    def year(self) -> int:
        return self._year
    
    @year.setter
    def year(self, new_year) -> None:
        self._year = new_year

    @property
    def speed(self) -> int:
        return self._speed
    
    @speed.setter
    def speed(self, new_speed) -> None:
        self._speed = new_speed

    # Methods

    @abstractmethod
    def accelerate() -> None:
        pass

    def stop(self) -> None:
        self._speed = 0

    @classmethod # forgot it
    def from_factory(cls, *args, **kwargs):
        return cls(*args, **kwargs)
    
    # Magic Methods

    def __str__(self):
        return f"{self.brand} {self.model} from {self.year} move at {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, door_nb: int, brand: str, model: str, year: int):
        super().__init__(brand, model, year)
        self.door_nb = door_nb

    # Getters / Setters
    @property
    def door_nb(self) -> int:
        return self.__door_nb
    
    @door_nb.setter
    def door_nb(self, new_door_nb) -> None:
        self.__door_nb = new_door_nb

    # Methods

    def accelerate(self) -> None:
        self.speed += 5

    # Magic Methods

    def __str__(self):
        return f"{self.brand} {self.model} with {self.door_nb} doors from {self.year} move at {self.speed} km/h"


class Motorbike(Vehicle):
        # not needed because no new attributes
        # def __init__(self, brand: str, model: str, year: int):
        #     super().__init__(brand, model, year)

        def accelerate(self) -> None:
            self.speed += 3

        def accrobatics(self) -> str:
            return "Wheel-in!"


# Properly doesn't work since it's an abstract class
# new_vehicle = Vehicle("citroen", "c2", 5)
# print(new_vehicle)

# Car properly seems to work
citroen = Car(4 ,"citroen", "c2", 5)
print(citroen) # shows the car info except doors
print(citroen.door_nb) # getter works
citroen.accelerate()
print(citroen) # properly sped up

harley = Motorbike("Davidson", "Harley", 7)
print(harley)
harley.accelerate()
harley.accelerate()
harley.accelerate()
print(harley) # properly accelarated three times
print(harley.accrobatics())