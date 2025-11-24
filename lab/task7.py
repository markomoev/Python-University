class Car:
    def __init__ (self, id, brand, model, year, base_price, milage, gas_type, needed_lic):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.base_price = base_price
        self.milage = milage
        self.gas_type = gas_type
        self.needed_lic = needed_lic

    def rental_price(self, days):
        self.days = days
        return self.base_price * days

    def is_available(self, availability):
        self.availability = availability
        availability = True
        
    
    def car_info(self):
        return f"{self.brand} - {self.model} - {self.year} - {self.milage}"
    
class Economoy(Car):
    def calculate_price(self, days):
        return super().rental_price(days) * 0.9
    
class Premium(Car):
    def calculate_price(self, days):
        return super().rental_price(days) * 1.5
    
class SUV(Car):
    def calcualate_price(self, days):
        return super().rental_price(days) * 1.3
    
class Electric(Car):
    def calculate_price(self, days):
        return super().rental_price(days) * 0.8


# Customers
class Customer(Car):
    def __init__(self, name, phone, email, lic_category, reserv):
        self.name = name
        self.phone = phone
        self.email = email
        self.lic_category = lic_category

        self.reserv = reserv
        reserv = []
        
    def can_rent(self, needed_lic):
        if self.lic_category == needed_lic:
            return True
        
    def add_reserv(self, reserv, name):
        if super().can_rent() == True:
            return reserv.append(name)
        else:
            print("Customer not fitting the reservation rules!")


# Reservations
class Reservation:
    def __init__(self, car, customer, days, final_price, status):
        self.car = car
        self.customer = customer
        self.days = days
        self.final_price = final_price
        self.status = status

    def set_status(self, status):
        self.status = status
        if status == "pending" or status == "active":
            self.car.availability = False
        elif status == "canceled":
            self.car.availability = True