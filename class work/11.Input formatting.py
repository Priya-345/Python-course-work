#Input formatting
#1. String Input
name = input("Enter your name: ")
print(name) #Enter your name: priyanka =priyanka5

#2. Integer Input
quantity = int(input("Enter the number of items: "))
print(quantity) #Enter the number of items: 5=5

#3. Float Input
price = float(input("Enter the product price: "))
print(price) #Enter the product price: 299.55=299.5

#4. Input as List (Space-separated)
names = input("Enter employee names (space-separated):").split()
print(names) #Enter employee names (space-separated): Ankit Ravi Sneha=['Ankit', 'Ravi', 'Sneha']    

#5. Input as List (Comma-separated)
tags = input("Enter tags (comma-separated): ").split(',')
print(tags) #Enter tags (comma-separated): sale,discount,new=['sale', 'discount', 'new']

#6. List of Integers
marks = list(map(int, input("Enter marks: ").split()))
print(marks) #Enter marks: 89 76 94 82=[89, 76, 94, 82]

#7.List of Floatsp
weights = list(map(float, input("Enter weights: ").split()))
print(weights) #Enter weights: 55.6 66.6 77.8 =[55.5, 66.6, 77.8]

#8. Tuple Input
dimensions = tuple(map(int, input("Enter length, width,height: ").split()))
print(dimensions) #Enter length, width, height: 10 20 15 =(10, 20, 15)

#9. Set Input
selected_ids = set(map(int, input("Enter selected image IDs:").split()))
print(selected_ids) #Enter selected image IDs: 101 102 103 101 104={104, 101, 102, 103}

#10. Dictionary Input using eval()
profile = eval(input("Enter user profile as a dictionary: "))
print(profile) #Enter user profile as a dictionary: {'name': 'Ravi', 'age':30, 'role': 'admin'}={'name': 'Ravi', 'age': 30, 'role': 'admin'}

#11. Multiple Inputs with Unpacking
username, password = input("Enter username and password:").split()
print("Username:", username)
print("Password:", password) #Enter username and password: user01 mypassword123=Username: user01,Password: mypassword123
