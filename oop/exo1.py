class Animal:
    population = 0

    def __init__(self, name : str, age: int):
        Animal.population += 1
        self.name = name
        self.age = age
    
    def shout():
        pass

    @staticmethod
    def animal_number():
        return Animal.population


chien = Animal("chien", 5)
chat = Animal("chat", 7)

print(chien.name, chien.age)
print(chat.name, chat.age)
print(Animal.population)
print(Animal.animal_number())