#1.lambda Function
#var=lambda para/argv:exp
u=lambda n:n+10
print(u(10))
#20

cube = lambda n:n**3
print(cube(5))
#125

s = lambda s: s[0]
print(s("Python"))
print(s("Lambda"))
#P
#L

add=lambda a,b:a+b
print(add(10,20))
print(add(100,20))
#30
#120

greater = lambda a,b: a if a>b else b
print(greater(20,30))
print(greater(40,60))
#30
#60

evenorodd=lambda n:"Even" if n%2==0 else "Odd"
print(evenorodd(15))
print(evenorodd(30))
#Odd
#Even

sumof3number= lambda a,b,c:a+b+c
print(sumof3number(10,20,30))
#60

#map using lambda Function

s="python programming"
changestr=list(map(lambda i:i.upper(),s))
print(changestr)
#['P', 'Y', 'T', 'H', 'O', 'N', ' ', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']

asci=list(map(lambda i:ord(i), s))
print(asci)
#[112, 121, 116, 104, 111, 110, 32, 112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]

vol='aeiouAEIOU'
frmt=list(map(lambda i:'*' if i in vol else '0',s ))
print(frmt)
#['0', '0', '0', '0', '*', '0', '0', '0', '0', '*', '0', '0', '*', '0', '0', '*', '0', '0']

l=[1,2,3,4,5,6,7,8,9,10]
lstup = list(map(lambda i:i+1,l))
print(lstup)
#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

t=(10,20,30,40,50,12,34,55,89)
tupup = tuple(map(lambda i:i//10,t))
print(tupup)
#(1, 2, 3, 4, 5, 1, 3, 5, 8)

s={'python','html','css','java','mysql'}
setup = set(map(lambda i:i.upper(),s))
print(setup)
#{'CSS', 'HTML', 'PYTHON', 'JAVA', 'MYSQL'}

#Filter using lambda Function

ffmrt = list(filter(lambda i: i in vol, s))
print(ffmrt)
#[]

cfrmt = list(filter(lambda i: i not in vol,s))
print(cfrmt)
#['python', 'java', 'mysql', 'css', 'html']


elst = list(filter(lambda i: i%2==0 ,l ))
print(elst)
#[2, 4, 6, 8, 10]

olst = list(filter(lambda i: i%2!=0 ,l ))
print(olst)
#[1, 3, 5, 7, 9]

divtup = tuple(filter(lambda i: i%10==0,t))
print(divtup)
#(10, 20, 30, 40, 50)

stset = set(filter(lambda i:i.startswith('p'),s))
print(stset)
#{'python'}