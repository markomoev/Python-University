class Market:
    def __init__(self, barcod, name, manufacturer, price, quantity):
        self.barcod = barcod
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity
    
    def sale(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
    
    def discount(self):
        if self.price >= 30 and self.price <= 50:
            self.price *= 0.95

        elif self.price >= 10 and self.price <= 30:
            self.price *= 0.93
        
    def display_info(self):
        print(self.barcod, self.name, self.manufacturer, self.price, self.quantity)

# main operations
def search_by_barcod(product_list, code):
    found = False
    aval_barcodes = []

    for p in product_list:
        if p.barcod == code:
            p.display_info()
            found = True
        else: 
            aval_barcodes.append(p.barcod)


    if found == False: 
        print("Wrong barcod !!!")
        print(f"Availible barcodes: ", aval_barcodes)



def search_by_manifacturer(product_list, manuf):
    sum_prices = 0
    count = 0

    for p in product_list:
        if p.manufacturer == manuf:
            sum_prices += p.prices
            count += 1

    avg_price = sum_prices / count

    result = []
    for p in product_list:
        if p.manufacturer == manuf and p.price <= avg_price:
            result.append(p)

    return result
        

def sort_by_quantity(product_list):        
    
    print(product_list.sort(key = lambda p: p.quantity, reverse = True))

def delete_by_name(product_list, name):
    for p in product_list:
        if p.name == name and p.quantity <= 3:
            product_list.remove(p)


# main programm, so we can fill up the list as we should be
product_list = []
try: 
    n = int(input("Enter a whole number: "))
except ValueError:
    n = 0
    print("Invailid number!")

for i in range(n):
    print("--- Enter the product details ---")
    p_code = int(input("Barcode:"))
    p_name = input("Product name: ")
    p_manuf = input("Manufacturer name: ")
    p_price = float(input("Price: "))
    p_qty = int(input("Quantity: "))

    new_product = Market(p_code, p_name, p_manuf, p_price, p_qty)
    new_product.discount()

    product_list.append(new_product)