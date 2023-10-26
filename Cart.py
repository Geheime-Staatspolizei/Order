import csv
from Product import Product

class Cart:
    userCartsPath = "./userCarts/"
    productFilePath = "products.csv"

    def __init__(self):
        pass

    def addProduct(self,userName,productId):
        product = self.checkProduct(productId)

        if product == False:
            return "Product is absent"
        
        self.writeProduct(userName,product)
        return "OK"

    def deleteProduct(self,userName,productId):
        product = self.checkProduct(productId)

        if product == False:
            return "Product is absent"
        
        self.cleanProduct(userName,productId)
        return "OK"

    def showCart():
        pass

    def checkProduct(self,productId):
        with open(self.productFilePath,'r') as file:
            fileReader = csv.reader(file)

            for product in fileReader:
                if product[0] == productId:
                    return Product(product[0],product[1],product[2])
            return False

    def writeProduct(self,userName,product):
        filePath = self.userCartsPath + userName + ".csv"
        file = open(filePath,'a',newline="")
        
        fileWriter = csv.writer(file)
        fileWriter.writerow(product.returnProduct())
        file.close()


    def cleanProduct(self,userName,productId):
        listOfProducts = []
        filePath = self.userCartsPath + userName + ".csv"
        file = open(filePath,'r',newline="")
        fileReader = csv.reader(file)

        for product in fileReader:
            listOfProducts.append(product[0])
        file.close()
        
        file = open(filePath,"w",newline="")
        fileWriter = csv.writer(file)

        for idProduct in listOfProducts:
            if idProduct != productId:
                fileWriter.writerow(self.checkProduct(idProduct).returnProduct())
        file.close
