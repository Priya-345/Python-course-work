# Vehicle Information System

# Task 1: Take Vehicle Details as Input

vehicle_id = int(input("Enter Vehicle ID: "))
vehicle_name = input("Enter Vehicle Name: ")
price = float(input("Enter Vehicle Price: "))

# List
categories = [cat.strip() for cat in input("Enter Vehicle Categories (comma-separated): ").split(',')]

# Tuple
stock_available = int(input("Enter Stock Available: "))
stock_sold = int(input("Enter Stock Sold: "))
stock_details = (stock_available, stock_sold)

# Float
discount_percentage = float(input("Enter Discount Percentage: "))

# Set
features = set(f.strip() for f in input("Enter Vehicle Features (comma-separated): ").split(','))

# Dictionary
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}

# Task 2: Display Vehicle Details Using Formatting

print("\n--- Vehicle Information ---")

# 1. Comma Separation (sep=',')
print("Vehicle ID, Name, Price:", vehicle_id, vehicle_name, price, sep=',')

# 2. Percentage Formatting (% operator)
print("Discount Offered: %.2f%%" % discount_percentage)

# 3. f-strings (f"")
print(f"Vehicle Name: {vehicle_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")
print(f"Vehicle Categories: {categories}")
print(f"Features: {features}")

# 4. .format() method
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details["Name"], supplier_details["Contact"], supplier_details["Location"]
))

#Enter Vehicle ID: 301  
#Enter Vehicle Name: Swift ZXI  
#Enter Vehicle Price: 829999.99  
#Enter Vehicle Categories (comma-separated): Hatchback, Petrol, Manual  
#Enter Stock Available: 40  
#Enter Stock Sold: 18  
#Enter Discount Percentage: 7.5  
#Enter Vehicle Features (comma-separated): ABS, Airbags, Touchscreen, Alloy Wheels  
#Enter Supplier Name: Maruti Showroom  
#Enter Supplier Contact Number: 98789234567, 
#Enter Supplier Location: Hyderabad


#--- Vehicle Information ---
#Vehicle ID, Name, Price:,301, Swift ZXI  ,829999.99
#Discount Offered: 8.00%
#Vehicle Name:  Swift ZXI
#Price: ₹829999.99
#Discount: 8.0%
#Stock Available: 40 units
#Vehicle Categories: ['Hatchback', 'Petrol', 'Manual']
#Features: {'Airbags', 'Touchscreen', 'ABS', 'Alloy Wheels'}
#Supplier Details: Name - Maruti Showroom  , Contact - 98789234567, Location - Hyderabad