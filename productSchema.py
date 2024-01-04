class Product:
    def __init__(self,pid,name,price,desc):
        self.__pid=pid
        self.name=name
        self.price=price
        self.desc=desc

    def display(self):
        print("PID: ", self.__pid)
        print("NAME: ", self.name)
        print("PRICE: ", self.price)
        print("DESCRIPTION: ", self.desc)

    def updatePid(self, pid):
        self.__pid = pid

    def updateName(self, name):
        self.name = name

    def updatePrice(self, price):
        self.price = price

    def updateDesc(self, desc):
        self.desc = desc

    def getPID(self):
        return self.__pid
