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
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name) -> None:
        if len(new_name) >= 2:
            self._name = new_name
        else:
            raise ValueError(f"Name should have at least two characters: {new_name}")

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age) -> None:
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
    # pass # peut suffir car on ajoute pas de nouvelles propriétés
    def __init__(self, name: str, age: int):
        super().__init__(name, age) 

    def shout() -> None:
        return "Woof!"
    
    @classmethod
    def from_factory(cls, name, age):
        if len(name) >= 3 and age > 0:
            return cls(name, age)
        else:
            raise ValueError(f"name should be at least 3 characters : {name} and age above 0 : {age}")
        

nord = Animal("nord", 7)
roger = Chien("roger", 5)

print(roger.name, roger.age)
print(nord.name, nord.age)
print(Animal.population)
print(Animal.animal_number())
print(roger)