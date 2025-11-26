class Books:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def get_info(self):
        return f"{self.title} - {self.author} - {self.price}"
    
    def apply_discount(self):
        return self.price
    
class Fiction(Books):
    def apply_discount(self):
        return self.price * 0.9
    
class NonFiction(Books):
    def apply_discount(self):
        return self.price * 1.05
    
class Comics(Books):
    def apply_discount(self):
        return self.price * 0.8
    
b1 = Fiction("Harry Potter", "J.K. Rowling", 50)
b2 = NonFiction("Sapiens", "Yuval Noah Harari", 60)
b3 = Comics("Spider-Man", "Stan Lee", 30)

print(b1.get_info(), "Price after discount:", b1.apply_discount())
print(b2.get_info(), "Price after discount:", b2.apply_discount())
print(b3.get_info(), "Price after discount:", b3.apply_discount())