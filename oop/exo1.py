class Animal:
    population: int = 0

    def __init__(self, name : str, age: int):
        Animal.population += 1
        self.name: str = name
        self.age: int = age
    
    def shout() -> None:
        pass

    @staticmethod
    def animal_number() -> int:
        return Animal.population


chien = Animal("chien", 5)
chat = Animal("chat", 7)

print(chien.name, chien.age)
print(chat.name, chat.age)
print(Animal.population)
print(Animal.animal_number())