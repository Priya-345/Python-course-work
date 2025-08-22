#
class shopping:
    discount=10
    def _init_(self,name):
        self.name=name
        self.orders=[]
    def myorder(self,order):
        self.orders.append(order)
        print(f"{self.name}!\nYour {self.orders}  is successfully placedd")
    @classmethod
    def updateDiscount(cls,newdiscount):
        cls.discount = newdiscount
        print(f'Updated discount:{cls.discount}')
    @staticmethod
    def Welcome():
        print("Welcome to E-cart. Have a great shopping time.")

sony=shopping('sony')
nikhitha=shopping('nikhitha')
sony.myorder('phone')
nikhitha.myorder('laptop')
sony.myorder('earrings')
nikhitha.myorder('jeans')
shopping.updateDiscount(15)
shopping.Welcome()
'''
class shopping:
    def _init_(self,username,phonenumber,password):
        self.username=username
        self.phonenumber=phonenumber
        self.password=password
        self.favs=[]
        self.orders=[]
        self.mycart=[]
        print(f"Welcome to Flipkart {self.username}. Enjoy the shopping")
revathi=shopping('revathi','2467892025','revathi@123')
#Welcome to Flipkart revathi. Enjoy the shopping
'''