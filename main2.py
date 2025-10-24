class computer:
    def __init__(self):
        self.max_price = 900
    def sell(self):
        print("Selling Price: {}".format(self.max_price))
    def setmaxprice(self, price):
        self.max_price = price
c = computer()
c.sell()
c.setmaxprice(2000)
c.sell()
