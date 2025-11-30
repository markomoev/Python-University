class Product:
    def __init__(self, name, base_price, category):
        self.name = name
        self.base_price = base_price
        self.category = category

    def get_info(self):
        return f"{self.name} ({self.category}) for {self.final_price()}"
    
    def final_price(self):
        return self.base_price
    
class Electronics(Product):
    def final_price(self):
        return super().final_price() + 20
    
class Clothes(Product):
    def final_price(self):
        return super().final_price() * 0.9
    
class Food(Product):
    def final_price(self):
        return super().final_price() * 1.05

# shopping cart functions
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def list_products(self):
        return self.items

    def total_price(self):
        total = 0
        for a in self.items:
            current = a.final_price()
            total += current
        return total
    
    def find_by_category(self):
        electronics_category = []
        clothes_category = []
        food_category = []

        for b in self.items:
            if b.category.lower() == 'electronics':
                electronics_category.append(b)
            if b.category.lower() == 'clothes':
                clothes_category.append(b)
            if b.category.lower() == 'food':
                food_category.append(b)

        return electronics_category, clothes_category, food_category
    
# test
p1 = Electronics("Laptop", 1200, "Electronics")
p2 = Clothes("T-Shirt", 30, "Clothes")
p3 = Food("Apple", 2, "Food")
p4 = Electronics("Headphones", 100, "Electronics")
p5 = Clothes("Jeans", 80, "Clothes")

cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.add_product(p4)
cart.add_product(p5)

cart.list_products()
print("Total:", cart.total_price())

electr, clothes, food = cart.find_by_category()
print("Electronics products:")
for e in electr:
    print(e.get_info())