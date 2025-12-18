from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int, speed: int = 0):
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.speed: int = speed

    def __str__(self):
        return f"{self.brand} {self.model} from {self.year} move at {self.speed} km/h"
    
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


    @abstractmethod
    def accelerate() -> None:
        pass

    def stop(self) -> None:
        self._speed = 0

    def from_factory(cls, *args, **kwargs):
        return cls(*args, **kwargs)
    


class Car(Vehicle):
    def __init__(self, door_nb: int, brand: str, model: str, year: int, speed: int = 0):
        super().__init__(brand, model, year, speed)
        self.door_nb = door_nb

    
    @property
    def door_nb(self) -> int:
        return self.__door_nb
    
    @door_nb.setter
    def door_nb(self, new_door_nb) -> None:
        self.__door_nb = new_door_nb

    def accelerate(self):
        self.speed += 5


class Motorbike(Vehicle):
        def __init__(self, brand: str, model: str, year: int, speed: int = 0):
            super().__init__(brand, model, year, speed)

        def accelerate(self):
            self.speed += 3

        def accrobatics():
            print("Wheel-in!")