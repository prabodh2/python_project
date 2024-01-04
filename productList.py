from packages.productSchema import Product

class ProductList:

    products = []

    def __init__(self):
        pass
    
    def __checkIsAdmin(self, isAdmin):
        if not isAdmin:
            print("ProductList denied!!!")
            return 0
        return 1

    def createProduct(self, isAdmin):
        if not isAdmin:
            print("Premission denied!!!")
            return 0
        pid = len(ProductList.products) + 1
        name = input("Product Name: ")
        price = int(input("Product Price: "))
        desc = input("Product Description: ")
        tempProduct = Product(pid,name, price, desc)
        ProductList.products.append(tempProduct)

    def displayProducts(self):
        if len(ProductList.products):
            for i in ProductList.products:
                i.display()
        else:
            print("No products to display!!!")
            return 0

    def __searchProduct(self, pid):
        tempProducts = ProductList.products
        index = None
        for i in range(len(tempProducts)):
            if tempProducts[i].getPID() == pid:
                index = i
                break

        return index

    def updateProduct(self, isAdmin, pid):
        if not isAdmin:
            print("Premission denied!!!")
            return 0
        tempProducts = ProductList.products
        index = self.__searchProduct(pid)
        if (index == None):
            print("Product not found!!!")
            return 0
        feild = input("Enter feild: ").lower()
        data = input("Enter updated Data: ")
        if feild == "name":
            tempProducts[index].updateName(data)
        elif feild == "price":
            data = int(data)
            tempProducts[index].updatePrice(data)
        elif feild == "description":
            tempProducts[index].updateDesc(data)
        else:
            print("Invalid Reponse")
            return 0
        ProductList.products=tempProducts
        print("Product updated")
        return 1

    def deleteProduct(self,isAdmin, pid):
        if (self.__checkIsAdmin(isAdmin)):
            tempProducts = ProductList.products
            index = self.__searchProduct(pid)
            tempProducts.pop(index)
            ProductList.products = tempProducts
