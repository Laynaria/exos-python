from abc import ABC, abstractmethod

class Animal(ABC):
    population: int = 0

    def __init__(self, name : str, age: int):
        Animal.population += 1
        self.name: str = name
        self.age: int = age
    
    def __str__(self) -> str:
        return f"{self.name.capitalize()} ({self.age} ans)"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) >= 2:
            self._name = new_name
        else:
            raise ValueError(f"Name should have at least two characters: {new_name}")

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError(f"Age should at least be 0 years : {new_age}")
    
    @abstractmethod
    def shout() -> None:
        pass

    @staticmethod
    def animal_number() -> int:
        return Animal.population
    
    

class Chien(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age) 

    def shout() -> None:
        return "Woof!"
    
    # @classmethod
    # def from_factory(name, age):
        

nord = Animal("nord", 7)
roger = Chien("roger", 5)

print(roger.name, roger.age)
print(nord.name, nord.age)
print(Animal.population)
print(Animal.animal_number())
print(roger)

