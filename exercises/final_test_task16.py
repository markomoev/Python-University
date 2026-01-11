class Market: 
    def __init__(self, barcode, name, manufacturer, price, quantity):
        self.barcode = barcode
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity
    
    def product_info(self):
        print(f"Barcode:{self.barcode}, Name:{self.name}, Manufacturer:{self.manufacturer}, Price:{self.price}, Quantity:{self.quantity}")

    def change_barcode(self):
        self.barcode = int(input("Enter a new number for the barcode: "))

    def change_quantity(self):
        self.quantity = int(input("Enter the new quantity: "))

product_list = []
p1 = Market(12, "Enrico", "ltb", 55, 5)
p2 = Market(13, "Diego", "Lewis", 90, 10)
p3 = Market(14, "Darien", "Hugo", 200, 2)
product_list.append(p1)
product_list.append(p2)
product_list.append(p3)

def search_by_barcode(product_list = product_list, barcode = int(input("Search for barcode... "))):
    for p in product_list:
        if p.barcode == barcode:
            p.product_info()
        else: 
            print("There is no such product!")

def search_by_man(product_list = product_list, manufacturer = str(input("Search for barcode... "))):
    for p in product_list:
        if p.manufacturer == manufacturer:
            p.product_info()
        else: 
            print("There is no such product!")


def sell_product_by_name(product_list = product_list, name = str(input("Enter the name: ")), num = int(input("Enter how much you want to sell: "))):
    for p in product_list:
        if p.name == name:
            if p.quantity >= num:
                print("Successful sale!", p.qunatity - num)
            else: 
                print("Unsuficient quantity!")
        else: 
            print("There is no such product!")