class Animal:
    def __init__(self, name, species, age, owner, base_price):
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self.base_price = base_price

    def get_info(self):
        return f"{self.name} ({self.species}, age:{self.age}, owner:{self.owner})"
    
    def calculate_visit_price(self):
        return self.base_price
    
#animals sublcalsses
class Dog(Animal):
    def __init__(self):
        return self.base_price + 20
    
class Cat(Animal):
    def __init__(self):
        return self.base_price * 0.9

class Bird(Animal):
    def __init__(self):
        return self.base_price + 5

# clinic
class Clinic:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def add_animal(self, animal):
        if len(self.patients) < self.capacity:
            self.patients.append(animal)
            return f"{animal.name} was admitted"
        return "Clinic is full"
    
    def list_animals(self):
        for a in self.patients:
            print(a.get_info())

    def get_total_animals(self):
        return len(self.patients)
    
    def total_revenue(self, days = 1):
        total = 0
        for a in self.patients:
            total += a.calculate_price() * days
        return total
    
    def get_info(self):
        return f"{self.name} - capacity: {self.capacity}, current: {self.get_total_animals()}"
    
a1 = Animal("Rex", "Dog", 5, "Ivan", 30)
a2 = Animal("Molly", "Cat", 3, "Petya", 25)
a3 = Animal("Bunny", "Rabbit", 2, "Maria", 20)
a4 = Animal("Gei", "Kaninchen", 4, "Pedalski", 8)

clinic = Clinic("Happy Pets", 3) 

print(clinic.add_animal(a1))
print(clinic.add_animal(a2))
print(clinic.add_animal(a3))
print(clinic.add_animal(a4))  

print(clinic.get_total_animals())
print(clinic.get_info())