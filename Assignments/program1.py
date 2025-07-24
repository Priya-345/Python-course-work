# Amazon Order System

# Input Section
order_id = int(input("Enter Order ID: "))
customer_name = input("Enter Customer Name: ")
order_total = float(input("Enter Total Amount: "))

# List input
ordered_items = [item.strip() for item in input("Enter Ordered Items (comma-separated): ").split(',')]

# Tuple input
shipping_address = (
    input("Enter Delivery City: "),
    input("Enter Zip Code: ")
)

# Float input
discount_percent = float(input("Enter Discount Percentage: "))

# Set input
payment_modes = set(mode.strip() for mode in input("Enter Payment Methods Used (comma-separated): ").split(','))

# Dictionary input
seller_name = input("Enter Seller Name: ")
seller_rating = input("Enter Seller Rating (e.g., 4.5/5): ")
seller_details = {
    "Seller": seller_name,
    "Rating": seller_rating
}

# Output Section
print("\n--- Amazon Order Summary ---")

# 1. Comma Separation (sep=',')
print("Order ID, Customer, Amount:", order_id, customer_name, order_total, sep=',')

# 2. Percentage Formatting (%)
print("Discount Applied: %.2f%%" % discount_percent)

# 3. f-strings (f"")
print(f"Customer Name: {customer_name}")
print(f"Items Ordered: {ordered_items}")
print(f"Delivery Address: {shipping_address[0]} - {shipping_address[1]}")
print(f"Payment Methods Used: {payment_modes}")

# 4. .format() method
print("Seller Details: Name - {}, Rating - {}".format(
    seller_details["Seller"], seller_details["Rating"]
))

#Enter Order ID: 99881
#Enter Customer Name: Priyanka
#Enter Total Amount: 5499.75
#Enter Ordered Items (comma-separated): Laptop Bag,Mouse
#Enter Delivery City: Bengaluru
#Enter Zip Code: 560001
#Enter Discount Percentage: 12.5
#Enter Payment Methods Used (comma-separated): Credit Card,Amazon Pay
#Enter Seller Name: Cloud
#Enter Seller Rating (e.g., 4.5/5): 4.6/5

#--- Amazon Order Summary ---
#Order ID, Customer, Amount:,99881,Priyanka,5499.75
#Discount Applied: 12.50%
#Customer Name: Priyanka
#Items Ordered: ['Laptop Bag', 'Mouse']
#Delivery Address: Bengaluru - 560001
#Payment Methods Used: {'Amazon Pay', 'Credit Card'}
#Seller Details: Name - Cloud, Rating - 4.6/5