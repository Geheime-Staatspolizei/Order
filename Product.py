class Product:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

    def returnProduct(self):
        return [self.id,self.name,self.price]