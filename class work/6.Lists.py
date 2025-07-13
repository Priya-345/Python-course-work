# 1.Creating Lists
#Empty List
my_list = []
my_list = list()

#List with elements
n = [1,2,3,4,5,6,7,8]
print(n) #[1, 2, 3, 4, 5, 6, 7, 8]

# 2. Accessing Elements in a List
# Using Indexing (Positive & Negative)
n1 = [1,2,3,4,5,6,7,8,9]
print(n1[0]) #1
print(n1[3]) #4
print(n1[-1]) #9

# Using Slicing
number = [10,20,30,40,50]
print(number[1:4]) #[20, 30, 40]
print(number[3:])   #[40, 50]
print(number[-4:-1]) #[20, 30, 40]
print(number[::-1]) #[50, 40, 30, 20, 10]
print(number[-3:]) #[30, 40, 50]

# 3.Modifying List
# Adding Elements
number = [10,20,40,50,70,80,100]
number.append(120) #[10, 20, 40, 50, 70, 80, 100, 120]

# 4.List Methods
# Append
number1 = [10,20,30,50,80,110]
number1.append(3.45)
number1.append(4+3j)
number1.append("Rama")
number1.append({1,2,3,4,5})
number1.append({'name':'Rama','subject':'english'})
print(number1) #[10, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}, {'name': 'Rama', 'subject': 'english'}]

# Insert 
number2 = [10, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}]
number2.insert(1,25)
print(number2) #[10, 25, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}]

# Extend(adds multiple elements)
number3 = [10, 25, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}]
number3.extend([45,55,65,75]) #[10, 25, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}, 45, 55, 65, 75]
print(number3)

# Changing Elements
number = [1,2,3,4,5,6,7,8,9,10]
number[9] = 110
print(number) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 110]

# Removing Elements
number5 = [10, 25, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}, 45, 55, 65, 75]
number5.remove(75)
print(number5) #[10, 25, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}, 45, 55, 65]

# pop
number6 = [10, 25, 20, 30, 50, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}, 45, 55, 65]
number6.pop(4)
number6.pop()
print(number6) #[10, 25, 20, 30, 80, 110, 3.45, (4+3j), 'Rama', {1, 2, 3, 4, 5}, 45, 55]

# del
fruits = ['apple','banana','cherry']
del fruits[1]
print(fruits) #['apple', 'cherry']

# clear
fruits = ['apple', 'cherry']
fruits.clear()
print(fruits) #[]

# count
number7 = [1,2,3,4,7,2,4,6,8,1,9,4,2,4,6,7,4]
print(number7.count(4)) #5

# Index
number8 = [1,4,5,10,20,25,30,38,40,80]
l = number8.index(80)
print(l) #9

# sorted
number9 = [1,5,2,6,3,8,19,17,3,4,25,15,30]
print(sorted(number9)) #[1, 2, 3, 3, 4, 5, 6, 8, 15, 17, 19, 25, 30] 

# sort
number10 = [1,5,2,6,3,8,19,17,3,4,25,15,30]
number10.sort()
print(number10) #[1, 2, 3, 3, 4, 5, 6, 8, 15, 17, 19, 25, 30]

# reverse
number11 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
number11.reverse()
print(number11) #[13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Copy
number12 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
m=number12.copy()
print(m) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

n=number12
n.append(18)
print(n) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18]

# Max,min,len,any,all
number13 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18]
print(max(number13)) #18
print(min(number13)) #1
print(len(number12)) #16
print(any(number13)) #True
print(all(number13)) #True
