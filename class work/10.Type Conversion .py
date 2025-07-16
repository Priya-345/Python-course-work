# Type Conversion (Type Casting)
#1. Converting from int
#float
a = 2
print(float(a)) #2.0

#string
print(str(a)) #2

#boolean
print(bool(a)) #True

#list
# print(list(a)) #error

#set
# print(set(a)) #error

#tuple
# print(tuple(a)) #error

#dictionary
# print(dict(a)) #error

#2. Converting from float
#integer
n = 3.1
print(int(n)) #3 

#string
print(str(n)) #3.1

#boolean
print(bool(n)) #True

#list
# print(list(n))

#set
# print(set(n)) #error

#tuple
# print(tuple(n)) #error

#dictionary
# print(dict(n )) #error

#3. Converting from str
#integer
S = 'hello'
#print(int(S)) #error
c = '10'
print(int(c)) #10

#float
# print(float(S)) #error
print(float(c)) #10.0

#boolean
print(bool(S)) #True

#list
print(list(S)) #['h', 'e', 'l', 'l', 'o']

#set
print(set(S)) #{'o', 'h', 'l', 'e'}

#tuple
print(tuple(S)) #('h', 'e', 'l', 'l', 'o')

#dictionary
# print(dict(S)) #error

#4. Converting from list
#iteger
d = [1,2,3,4]
# print(int(d)) #error

#float
# print(float(d)) #error

#str
print(str(d)) #

#boolean
print(bool(d)) #True

#set
print(set(d)) #{1, 2, 3, 4}

#tuple
print(tuple(d)) #(1, 2, 3, 4)

#dictionary
# print(dict(S)) #error

#5. Converting from tuple
#integer
t = (1,2,3,4)
# print(int(t)) #error

#float
# print(float(t)) #error

#string
print(str(t)) #(1, 2, 3, 4)

#boolean
print(bool(t)) #True

#list
print(list(t)) #[1, 2, 3, 4]

#set
print(set(t)) #{1, 2, 3, 4}

#dictionary
# print(dict(d)) #error

#6. Converting from set
#integer
s = {3,4,5,6}
# print(int(s)) #error

#float
# print(float(s)) #error

#string
print(str(s)) #{3, 4, 5, 6}

#boolean
print(bool(s)) #True

#list
print(list(s)) #[3, 4, 5, 6]

#tuple
print(tuple(s)) #(3, 4, 5, 6)

#dictionary
# print(dict(s)) # error

#7. Converting from dict
#integer
d = {1: 1, 2: 4, 3: 9}
# print(int(d)) #error

#float
# print(float(d)) #error

#string
print(str(d)) #{1: 1, 2: 4, 3: 9}

#boolean
print(bool(d)) #True

#list
print(list(d)) #[1, 2, 3]

#tuple
print(tuple(d)) #(1, 2, 3)

#set
print(set(d)) #{1, 2, 3}
boolean = False
#8. Converting from bool
#integer
b = False
print(int(b)) #0

#float
print(float(b)) #0.0

#string
print(str(b)) #False

#list
# print(list(b)) #error

#tuple
# print(tuple(b)) #error

#set
# print(set(b)) #error

#dictionary
# print(dict(b)) #error

#9. Dictionary Conversion
d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
print(dict(d)) #{'name': 'teja', 'batch': '22', 'subject': 'python'}