##7.Tuple
#1.Tuple Creation
#1.1.Empty Tuple
empty_tuple = ()
print(empty_tuple) #()

#1.2.Single elemnet Tuple
t = (5,)
print(t) #5,

#1.3.Multi-element tuple
t1 = (1,"priyanka",2.6)
print(t1) #(1, 'priyanka', 2.6)

#1.4.Without parentheses
t2 = 1,2,3
print(t2) #(1, 2, 3)

#2.Accessing Tuple Elements
#2.1.Indexing
t3 = (10,20,30,40,50)
print(t3[1]) #20

#2.2.Negative Indexing
t4 = (10,20,30,40,50,60)
print(t4[-4]) #30

#2.3.Slicing
t5 = (10,20,30,40,50,60,70)
print(t4[2:5]) #(30, 40, 50)
print(t4[-3:-1]) #(40, 50)

#3.Operations on Tuple
#3.1.Concatenation
t5 = (1,2,3,4,5)
t6 = (6,7,8,9,10)
t7 = t5+t6
print(t7) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#3.2.Repetition 
t8 = (1,2,3,4)
print(t8*4) #(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

#3.3.Membership Testing
t9 = (1,2,3,4,5)
print(1 in t9) #True
print(6 not in t9) #True

#3.4 Tuple Unpacking
t10 = (1,2,3)
a,b,c = t10
print(a,b,c) #1 2 3

#4.Tuple Methods
#4.1.Count
t11 = (1,2,3,4,5,4,2,5)
print(t11.count(4)) #2

#4.2.index
t12 = (1,2,3,4,5)
print(t12.index(3)) #2

#5.Built-in Functions For Tuple
#5.1.len
t13 = (1,2,3,4,5,6,7,8,9)
print(len(t13)) #9

#5.2.max
t14 = (1,2,3,4,5,6,7,8,9)
print(max(t14)) #9

#5.3.min
t15 = (1,2,3,4,5,6,7,8,9)
print(min(t15)) #1

#5.4.sum
t16 = (1,2,3,4,5,6,7,8,9,10)
print(sum(t16)) #55

#6.Immutability and Tuple Behavior
nested_tuple = (1,[2,3])
nested_tuple[1][0] = 100
print(nested_tuple) #(1, [100, 3])