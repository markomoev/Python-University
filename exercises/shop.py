class Fruit:
    def __init__(self, name, price_per_kg, weight):
        self.name = name
        self.price_per_kg = price_per_kg
        self.weight = weight

    def get_info(self):
        return f"{self.name} for {self.price_per_kg} per 1kg. Total weight: {self.weight}"

    def total_price(self):
        return self.price_per_kg * self.weight
    
class Apple(Fruit):
    def total_price(self):
        return super().total_price() * 0.9

class Banana(Fruit):
    def total_price(self):
        return super().total_price() * 1.05
    
class Cherry(Fruit):
    def total_price(self):
        return super().total_price() * 0.8
    
# the shop
class Shop:
    def __init__(self, name):
        self.name = name
        self.fruits = []

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def list_fruits(self):
        for fruit in self.fruits:
            print(fruit.get_info())
    
    def calculate_total(self):
        total = 0
        for fruit in self.fruits:
            price = fruit.total_price()
            total += price
        return total
    
a1 = Apple("Green Apple", 3, 2)
b1 = Banana("Cavendish", 2, 5)     
c1 = Cherry("Black Cherry", 10, 1)

shop = Shop("Fruits R Us")
shop.add_fruit(a1)
shop.add_fruit(b1)
shop.add_fruit(c1)

shop.list_fruits()
print("Total price:", shop.calculate_total())
