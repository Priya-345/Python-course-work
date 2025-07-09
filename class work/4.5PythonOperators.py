#5. Membership Operators
#List
R = [10,20,30,40]
print(10 in R) #True
print(20 in R) #True
print(40 in R) #True
print(60 not in R) #True

#Tuple
T = (1,2,3,4,5,6,7,8) 
print(1 in T) #True
print(9 in T) #False
print(10 not in T) #True

#Dictionaries
Data = {"Name":"Priyanka","Age":"22","Course":"PFS"} 
print("Name" in Data) #True
print("Location"  not in Data) #True
print("Course" in Data) #True

#set
S = {1,2,3,4,5} 
print(1 in S) #True 
print(6  not in S) #True
print(7 in S) #False

#String 
S = "Priyanka"
print("k" in S) #True
print("P" not in S) #False