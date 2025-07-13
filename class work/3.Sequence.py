#3.Sequencetype
#1.1.String
a = "Hello"
print(a) #Hello
print(type(a)) #<class 'str'>

#1.2.List
cart_items = ["shoes","T-shirt","Headphones"]
print(cart_items) #['shoes', 'T-shirt', 'Headphones']
print(type(cart_items)) #<class 'list'>

#1.3.Tuple
c = (1,"Priyanka",2.4)
print(c) #(1, 'Priyanka', 2.4)
print(type(c)) #<class 'tuple'>

#2.Set Type
#2.1.Set
set = {1,2,3,4,5} 
print(set) #{1, 2, 3, 4, 5}
print(type(set)) #<class 'tuple'>

#2.2.Frozenset
frozen = frozenset([1,2,3])
print(frozen) #frozenset({1, 2, 3}) 

#3.Mapping Type
#3.1.Dictionary
dict = {'name':'Priyanka','age':23}
print(dict) #{'name': 'Priyanka', 'age': 23}
print(type(dict)) #<class 'dict'>

#4.Boolean
is_logged_in = True
is_payment_successful = False
is_in_stock = True
print(is_logged_in) #True
print(is_payment_successful) #False
print(is_in_stock) #True
print(type(is_in_stock)) #<class 'bool'>

#5.None Type
tracking_number = None
delivery_partner = None
print(tracking_number) #None 
print(delivery_partner) #None
print(type(tracking_number)) #<class 'NoneType'>