# Operations on Strings

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) #Hello World

# Repetition
string = "hello"
result = string * 3
print(result) #hellohellohello

# Indexing
text = "Hello World"
print(text[2]) #l
print(text[6]) #w

# Slicing
text = "Hello World"
print(text[0:6]) #Hello
print(text[:4]) #Hell
print(text[3:]) #lo World

# Membership
text = "Hello World"
print('Wor' in text)  #True
print('Java' not in text) #True