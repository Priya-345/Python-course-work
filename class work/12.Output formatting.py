# Output formatting
#1.Basic Examples of print()
#a) Printing Text
print("Hello, World!") #Hello, World!

#b) Printing Multiple Items
name = "Asha"
age = 25
print("Name:", name, "Age:", age) #Name: Asha Age: 25

#c) Using sep to Change the Separator
print("2024", "02", "07", sep="-") #2024-02-07

#d) Using end to Control Line Endings
print("Hello,", end=" ") #Hello,
print("World!") #World!

#2.Printing Special Characters
#a)New Line (\n):
print("Line 1\nLine 2") #Line 1 Line2

#b)Tab (\t):
print("Name:\tAlice") #Name:   Alice

#Output Formatting
#1)Using Commas (Simple Print Method)
name = "Alice"
age = 25
score = 95.5
# Using Commas
print("Name:", name, "Age:", age, "Score:", score) #Name: Alice Age: 25 Score: 95.5

#2)Using Modulo Operator (% Formatting)
name = "Bob"
age = 30
score = 88.75
# Using Modulo Operator
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score)) #Name: Bob | Age: 30 | Score: 88.75

#3)Using f-strings (Formatted String Literals)
name = "Charlie"
age = 28
score = 92.389
# Using f-strings
print(f"Name: {name} | Age: {age} | Score: {score:.2f}") #Name: Charlie | Age: 28 | Score: 92.39

#4)Using str.format() Method
name = "Diana"
age = 22
score = 89.456
# Using str.format()
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,score)) #Name: Diana | Age: 22 | Score: 89.5
