class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if self.stock>=quantity:
            print('The stock is available ')
        else:
            print('Stock is not available')
    def show(self):
        print(f'The name is{self.name},The price is: {self.price},The stock is:{self.stock}')
product=Product("Lenova",800,50)
product.show()
quantity_requested = int(input("Enter the quantity you want: "))
product.check_availability(quantity_requested)


        