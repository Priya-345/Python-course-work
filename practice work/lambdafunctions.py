# lambda functions
# 1. Square of a number using lambda 
# Question: Write a lambda function to return the square of a number.
square = lambda n: n*n
print(square(4))
print(square(2))
#16
#4


#2. Check if number is even using lambda
#Question: Write a lambda function that checks if a number is even.
evenorodd = lambda n: "even" if n%2 == 0 else "odd"
print(evenorodd(12))
print(evenorodd(13))

#even
#odd

#3. Get maximum of two numbers using lambda
#Question:Write a lambda function that returns the maximum of two numbers.
maxof2num = lambda a,b : a if a>b else b
print(maxof2num(12,45))
print(maxof2num(98,100))
#45
#100

#4. Multiply two numbers using lambda
#Question:Write a lambda function to multiply two numbers.
mul = lambda a,b : a*b
print(mul(2,3))
print(mul(10,8))
#6
#80

#5. Sort a list of tuples by second element using lambda
#Question: Sort a list of tuples by the second value using a lambda function.

l = [(1,3),(2,1),(4,2)]
print(sorted(l)) # based on first element
print(sorted(l,key = lambda i:i[1])) # sorting based on second element 
'''
[(1, 3), (2, 1), (4, 2)]
[(2, 1), (4, 2), (1, 3)]
'''

#6. Filter even numbers from a list using lambda and filter()
#Question: Use lambda with filter() to get even numbers from a list.

l = [1, 2, 3, 4, 5, 6] 
evenlist = list(filter(lambda i: i % 2 == 0 , l))
print(evenlist)

oddlist = list(filter(lambda i: i % 2 != 0 , l))
print(oddlist)
'''
[2, 4, 6]
[1, 3, 5]

=== Code Execution Successful ===
'''


#7. Square each element in a list using lambda and map()
#Question: Use lambda with map() to return squares of all elements in a list.

l = [1,2,3,4,5]
squ = list(map(lambda i:i*i,l))
print(squ)
# [1, 4, 9, 16, 25]


#8. Convert list of strings to uppercase using lambda
#Question: Use lambda with map() to convert all strings in a list to uppercase.

names = ["hello", "world"]
a = list(map(lambda i:i.upper(),names))
print(a)
# ['HELLO', 'WORLD']

#9. Sort list of dictionaries by key using lambda
#Question: Sort a list of dictionaries by the value of the 'age' key using lambda.










#10. Return length of a string using lambda
#Question: Write a lambda function that returns the length of a string.

s = "hello"
length = lambda s: len(s)
print(length(s))
#5


#11. Check if string starts with a vowel using lambda
#Question: Write a lambda function that checks if a string starts with a vowel.

vol = "aeiouAEIOU"
check = lambda s:True if s[0] in vol else False
print(check("apple"))
print(check("banana"))
#True
#False


#12. Add 10 to each element using lambda and map()
#Question: Use lambda with map() to add 10 to each number in a list.

l = [1,2,3]
listup=list(map(lambda i:i+10,l))
print(listup)
#[11, 12, 13]


#13. Filter strings longer than 3 characters
#Question: Use lambda with filter() to return only strings with more than 3 characters.

l = ["a", "the", "lamp", "cat"]
update = list(filter(lambda i: len(i) > 3,l))
print(update)
# ["lamp"]


#14. Multiply each number by its index using lambda
#Question: Use lambda with map() and enumerate() to multiply each element by its index.

l = [1,2,3,4]
for val , ind in enumerate(l):
    print(val,ind)
l1 = list(map(lambda val:val[0] * val[1],enumerate(l)))
print(l1)    

'''
0 1
1 2
2 3
3 4
[0, 2, 6, 12]
'''

#15. Use lambda with reduce() to calculate product
#Question: Use lambda with functools.reduce() to return the product of all numbers in a list.

from functools import reduce

l = [1,2,3,4,5,6,7]
product = reduce(lambda pro,items: pro*items, l)
print(product)
#5040

#16. Use lambda with filter to find multiples of 3
#Question: Use lambda with filter() to get numbers divisible by 3.

l = [1,2,3,4,5,6,7,8,9,10]
mulof3 = list(filter(lambda i: i % 3 ==0,l))
print(mulof3)
#[3,6,9]

#17. Sort words in a list by their length
#Question: Sort a list of words by their length using lambda.

#18. Lambda to extract domain from email
#Question: Write a lambda function to extract domain from email addresses.

domain = lambda mail: mail.split("@")[1]
print(domain("xyz@gmail.com"))
#gmail.com


#19. Use lambda to get last digit of a number
#Question: Write a lambda function that returns the last digit of a number.

lastdig = lambda n : n%10
print(lastdig(234))
#4


#20. Use lambda to check if year is a leap year
#Question: Write a lambda function that checks if a year is a leap year.

isleap = lambda year : "Leap year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not leap"
print(isleap(2025))
# Not leap