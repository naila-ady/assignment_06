"""Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to 
update it, and @price.deleter to delete it.

"""
class Product:
    def __init__(self, price):
        self._price = price  # private attribute with single underscore (convention)

    @property
    def price(self):        # Getter method
        print("Getting Price")
        return self._price

    @price.setter
    def price(self, value): # Setter method
        print("Setting Price")
        self._price = value

    @price.deleter
    def price(self):        # Deleter method
        print("Deleting Price")
        del self._price
        
        
product = Product("$800")              # Object banaya
print(product.price)                   # Getting Price → $800

product.price = "$1000"                # Setting Price
print(product.price)                   # Getting Price → $1000

del product.price                      # Deleting Price
# print(product.price)                # ❌ Error: AttributeError (kuyunki delete ho chuka hai)


    
    

