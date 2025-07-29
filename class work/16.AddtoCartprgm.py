#
data={
    "Apple":30,
    "Banana":10,
    "orange":20,
    "Milk":50,
    "Bread":25,
    "Eggs":60,
    "Rice":40,
    "Tea":35,
    "Sugar":20,
    "Salt":15
    }
# Bill generation
AddtoCart={}
while True:
    print('Available Products'.center(40,'='))
    for i,key in enumerate(data):
        print(f'{(i+1)}. {key.ljust(10," ")} : ${data[key]}')
# Taking a product name
    product = input("Enter the product name(Done-Exit): ").strip().lower()

# Exit-Bill Generation Logic
    if product=='Done':
        if AddtoCart:
            totalbill=0
            for i in AddtoCart:
                print(f'{i.ljust(10," ")} : {AddtoCart[i]} * {product[i]}')
                totalbill=totalbill+AddtoCart[i]*data[i]
                print(f"Total Bill : {totalbill}")
        else:
            print('Thanks')
        break
# Adding products to the cart
if product in data:
       qua = int(input("Enter the quantity: "))
       print(f'{product} is added to the cart')
       AddtoCart[product] = qua
else:
        print(f"{product} is not found")
