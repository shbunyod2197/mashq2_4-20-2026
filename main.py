# 1
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_price(self):
        print(f"{self.brand} narxi: {self.price}")

a = Phone("Iphone", "2500$")
a.show_price()

# 2
class Book:
    def __init__(self, title, auther):
        self.title = title
        self.auther = auther

    def about(self):
        print(f"Kitob: {self.title}, Muallif: {self.auther}")


a = Book("Python", "Aliyev")
a.about()
