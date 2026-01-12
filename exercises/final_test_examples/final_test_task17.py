class FoodDelivery:
    def __init__(self, order_number, destination, price, delivery_term, order_status):
        self.order_number = order_number 
        self.destination = destination
        self.price = price
        self.delivery_term = delivery_term
        self.order_status = order_status

    def order_info(self):
        print(f"Order num:{self.order_number}, Dest:{self.destination}, Price:{self.price}, Term:{self.delivery_term}, Status:{self.order_status}")

    def change_term(self):
        self.delivery_term = str(input("Enter a new delivery term: "))

order_list = []
while len(order_list) < 1:
    order_number = int(input("Enter a order number: "))
    destination = str(input("Enter a destination: "))
    price = float(input("Enter a price: "))
    delivery_term = str(input("Enter the date: "))
    order_status = str(input("Enter the status: "))

    order = FoodDelivery(order_number, destination, price, delivery_term, order_status)
    order.order_info()
    order_list.append(order)


def status_info(order_list = order_list, num = int(input("Enter the order number: "))):
    found = False
    status = ""
    for o in order_list:
        if o.order_number == num:
            found = True
            status = o.order_status
    if found:
        print("Found, ", status)
    else:
        print("Not Found")

def add_order(order_list = order_list):
    order_number = int(input("Enter a order number: "))
    destination = str(input("Enter a destination: "))
    price = float(input("Enter a price: "))
    delivery_term = str(input("Enter the date: "))
    order_status = str(input("Enter the status: "))

    new_order = FoodDelivery(order_number, destination, price, delivery_term, order_status)
    order_list.append(new_order)