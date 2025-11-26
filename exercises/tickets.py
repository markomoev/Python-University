class Ticket:
    def __init__(self, from_city, to_city, price):
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

    def get_info(self):
        return f"{self.from_city} - {self.to_city} for {self.price}"
    
    def final_price(self):
        return self.price
    
class BusTicket(Ticket):
    def final_price(self):
        return self.price * 0.9
    
class TrainTicket(Ticket):
    def final_price(self):
        return self.price * 1.05
    
class PlaneTicket(Ticket):
    def final_price(self):
        return self.price * 1.5
    
b1 = BusTicket("Sofia", "Plovdiv", 20)
b2 = TrainTicket("Varna", "Burgas", 30)
b3 = PlaneTicket("Sofia", "London", 100)

print(b1.get_info(), "Final price:", b1.final_price())
print(b2.get_info(), "Final price:", b2.final_price())
print(b3.get_info(), "Final price:", b3.final_price())
