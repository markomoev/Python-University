class ClothesShop:
    def __init__(self, product_id, product_type, product_brand, quantity):
        self.product_id = product_id
        self.product_type = product_type
        self.product_brand = product_brand
        self.quantity = quantity

    def display_info(self):
        print(f"Id:{self.product_id} Type:{self.product_type} Brand:{self.product_brand} Quantity:{self.quantity}")
# here we store all the products
clothes_list = []

product1 = ClothesShop(1, "T-Shirt", "LTB", 6)
product2 = ClothesShop(2, "Jeans", "Disquared2", 12)
product3 = ClothesShop(3, "Jacket", "Splendid", 4)

clothes_list.append(product1)
clothes_list.append(product2)
clothes_list.append(product3)

# operations

def search_by_id(clothes_list, id = int(input("Enter an id: "))):
    found = False
    for c in clothes_list:
        current_id = c.product_id
        if current_id == id:
            found = True
            break

    if found == True:
        c.display_info()
    else:
        print("There is no product with this id!")

search_by_id(clothes_list)

def search_by_brand(clothes_list, brand = str(input("Enter a brand: "))):
    found = False
    for c in clothes_list:
        current_brand = c.product_brand
        if current_brand.lower() == brand.lower():
            c.display_info()
            found = True

    if not found:
        print("There is no product with this brand!")

search_by_brand(clothes_list)

def sell_clothes_by_id(clothes_list, id = int(input("Enter an id: ")), num = int(input("Enter a quantity you want to buy: "))):
    found = False
    
    for c in clothes_list:
        current_id = c.product_id
        current_quantity = c.quantity

        if current_id == id:
            found = True
            if current_quantity > 0 and current_quantity >= num:
                c.quantity = current_quantity - num
                print("Successful sell")
                break
            else:
                print("The product is out of stock the quntity isn't enough!")
                break


    if found == False:
        print("Product not found!")

sell_clothes_by_id(clothes_list) 