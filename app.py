from flask import Flask
from Cart import Cart

app = Flask(__name__)
cart = Cart()

@app.route("/")
def index():
    return "Hello world!!"

@app.route("/add-product/<string:userName>/<string:productId>")
def addProduct(userName,productId):
    return cart.addProduct(userName,productId)

@app.route("/delete-product/<string:userName>/<string:productId>")
def deleteProduct(userName,productId):
    return cart.deleteProduct(userName,productId)