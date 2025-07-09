#6.Identity Operators
#Set
set1 = {1,2,3,4}
set2 = {1,2,3,4}
set3 = set1 
print(set1 is set2) #False
print(set1 is set3) #True

#List 
list1 = (1,2,3,4,5)
list2 = (1,2,3,4,5)
list3 = list2
print(list1 is list2) #True
print(list2 is list3) #True
print(list2 is not list3) #False

#String
str1 = "Priyanka"
str2 = "Priyanka"
Str3 = str1
print(str1 is str2) #True
print(str1 is not str2) #False
print(str1 is str2) #True

#Tuple
tuple1 = (1,2,3,4)
tuple2 = (1,2,3,4)
tuple3 = tuple1
print(tuple1 is  tuple2) #False
print(tuple1 is tuple3) #True

#Dictionaries
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'a':1,'b':2,'c':3}
dict3=dict1
print(dict1 is dict2 ) #False
print(dict1 is dict3) #True