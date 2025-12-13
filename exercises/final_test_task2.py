class Car: 
    def __init__ (self, car_brand, car_model, car_price, car_color, manifacture_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_price = car_price
        self.car_color = car_color
        self.manifacture_year = manifacture_year

    def display_info(self):
        return f"The car is: {self.car_brand} - {self.car_model}. It is from {self.manifacture_year}. We offer it in {self.car_color} color for {self.car_price}euro."


# list with exmaple cars    
car_list = []

car1 = Car("Opel", "Combo", 7000, "Grey", 2007)
car2 = Car("Volkswagen", "Golf", 11000, "White", 2011)
car3 = Car("BMW", "X6", 215000, "Grey", 2022)

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

if len(car_list) != 3:
    print("Sorry, but we don't have the space to store so much cars!")

# functions and operations
def sort_price():
    car_list.sort(key = lambda car: car.car_price, reverse=True)
    print(car_list)

def list_by_brand(brand = "Opel"):
    for car in car_list:
        if car.car_brand == brand:
            print(car.display_info())

def search_color(color = "Grey"):
    new_car_list = []
    for car in car_list:
        if car.car_color == color:
            new_car_list.append(car)
    new_car_list.sort(key = lambda car: car.car_price, reverse=True)
    print(new_car_list[0])

def newest_car():
    new_car_list = []
    for car in car_list:
        if car.manifacture_year == 2022:
            new_car_list.append(car)
    return new_car_list