##

from abc import ABC, abstractmethod

# ------------------------------
# Product (Encapsulation demo)
# ------------------------------
class Product:
    def __init__(self, sku, name, price):
        self.sku = sku             # public attribute
        self._name = name          # protected attribute
        self.__price = price       # private attribute

    # Getter (to access private price)
    def get_price(self):
        return self.__price

    # Setter (to modify private price safely)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("❌ Price must be positive")

    def __str__(self):
        return f"{self._name} (₹{self.__price})"

# ------------------------------
# Abstract Payment (Abstraction)
# ------------------------------
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

# ------------------------------
# Payment Subclasses (Inheritance + Polymorphism)
# ------------------------------
class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)   # super method
        self.card_number = card_number

    def pay(self):  # overriding abstract method
        print(f"✅ Paid ₹{self.amount} with Card ending {self.card_number[-4:]}")

class UpiPayment(Payment):
    def __init__(self, amount, vpa):
        super().__init__(amount)
        self.vpa = vpa

    def pay(self):  # overriding
        print(f"✅ Paid ₹{self.amount} with UPI {self.vpa}")

class CashOnDelivery(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):  # overriding
        print(f"💵 Pay ₹{self.amount} in cash upon delivery")

# ------------------------------
# User class with Class Method
# ------------------------------
class User:
    users = []  # class attribute

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        User.users.append(self)  # add to list

    @classmethod
    def total_users(cls):
        return len(cls.users)

# ------------------------------
# Order class (Composition)
# ------------------------------
class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.items = []

    def add_item(self, product, qty):
        self.items.append((product, qty))

    def total(self):
        return sum(p.get_price() * q for p, q in self.items)

    def checkout(self, payment: Payment):
        print(f"\n📦 Order {self.order_id} for {self.user.name}")
        for p, q in self.items:
            print(f" - {p} x {q}")
        print(f"Total: ₹{self.total()}")
        payment.pay()

# ------------------------------
# Demo / Execution
# ------------------------------
if __name__ == "__main__":
    # Create products
    iphone = Product("IPH-15", "iPhone 15", 79990)
    book = Product("BK-DSA", "DSA Handbook", 599)

    # Encapsulation: update price safely
    iphone.set_price(74990)

    # Create user
    user1 = User("U101", "Priya", "priya@example.com")
    print(f"👤 Total Users: {User.total_users()}")

    # Create order
    order = Order("ORD001", user1)
    order.add_item(iphone, 1)
    order.add_item(book, 2)

    # Payments (Polymorphism in action)
    order.checkout(CardPayment(order.total(), "1234567812345678"))
    order.checkout(UpiPayment(order.total(), "priya@upi"))
    order.checkout(CashOnDelivery(order.total()))