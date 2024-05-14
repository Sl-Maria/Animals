class Animal():
    def __init__(self, name, age, color, a_type):
        self.name = name
        self.age = age
        self.color = color
        self.a_type = a_type
    def make_sound(self):
        print("Grrrrrrr")
    def eat(self):
        print("Nom Nom Nom")

class Bird(Animal):
    def __init__(self, name, age, color, a_type, wing_span):
        super().__init__(name, age, color, a_type)
        self.wing_span = wing_span
    def make_sound(self):
        print("Crick Crick")

class Mammal(Animal):
    def __init__(self, name, age, color, a_type, fur_style):
        super().__init__(name, age, color, a_type)
        self.fur_style = fur_style
    def make_sound(self):
        print("Purr Purr")

class Reptile(Animal):
    def __init__(self, name, age, color, a_type, eye_color):
        super().__init__(name, age, color, a_type)
        self.eye_color = eye_color
    def make_sound(self):
        print("Sssssssss")

class Worker():
    def __init__(self, name, age,):
        self.name = name
        self.age = age
class ZooKeeper(Worker):
    def __init__(self, name, age,):
        super().__init__(name, age)
        self.occupation = "Keeper"
    def work(self):
        print("Кормлю животное")
class Veterinarian(Worker):
    def __init__(self, name, age,):
        super().__init__(name, age)
        self.occupation = "Vet"
    def work(self):
        print("Лечу животное")

class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.workers = []
    def add_animal(self, type, name, age, color, a_type):
        if type == 'bird':
            animal = Bird(name, age, color, a_type, 0.5)
        if type == 'mammal':
            animal = Mammal(name, age, color, a_type,'short')
        if type == 'reptile':
            animal = Reptile(name, age, color, a_type,'yellow')
        self.animals.append(animal)
    def remove_animal(self, animal):
        self.animals.remove(animal)
    def display_animals(self):
        for animal in self.animals:
            print(animal.name, animal.age, animal.color, animal.a_type)
    def add_worker(self, type, name, age):
        if type == 'keeper':
            worker = ZooKeeper(name, age)
        if type == 'vet':
            worker = Veterinarian(name, age)
        self.workers.append(worker)
    def remove_worker(self, worker):
        self.workers.remove(worker)
    def display_workers(self):
        for worker in self.workers:
            print(worker.name, worker.age, worker.occupation)


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

zoo = Zoo('Central Park')
zoo.add_animal('bird', 'Tweety', 2, 'blue', 'crow')
zoo.add_animal('mammal', 'Fluffy', 3, 'white', 'kangaroo')
zoo.add_animal('reptile', 'Lion', 4, 'green', 'lion')
zoo.display_animals()
zoo.add_worker('keeper', 'John', 35)
zoo.add_worker('vet', 'Jane', 25)
zoo.display_workers()

animal_sound(zoo.animals)