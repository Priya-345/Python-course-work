# Control Statements
#Bus seats booking
seats= {
    "U1":{'price':1029,'booking_status':False},
    "U2":{'price':1029,'booking_status':True},
    "U3":{'price':1029,'booking_status':True}

}
for i in seats:
    if seats[i]['booking_status']:
        print(f'*{i}*')
    else:
        print(f'{i}-{seats[i]["price"]}')
seatno = input("Enter the seat no:").upper()
if seatno in seats:
    if seats[seatno]['booking_status']:
        print(f"{seatno} is already booked. Go for other one!!")
    else:
        name = input("Enter the name:").title()
        age=int(input("Enter The age:"))
        gender = input("Enter The gender(F or M):").upper()
        if age<=5:
            print(f'Hello {name} your seat booked sucessfully with free of cost')
        elif age < 15:
            print(f'Hello {name} you seat booked sucessfully wth 50 % disscount\nTotal price={seats[seatno]["price"]*0.5}')
        else:
            print(f'Hello {name} you seat is booked suceccfull.pay the amount-{seats[i]["price"]}')      
else:
    print("Enter the seat no properly ")     



#Prime Number
n = int(input("Enter the Number: "))
c = 0
for i in range(2,n//2+1):
    if n%i==0:
        c=1
        break
if c==0:
    print("prime number")  
else:
    print("not a prime number")      
n = int(input("Enter the Number: "))
isprime = False
for i in range(2,n//2+1):
    if n%i==0:
        prime=True
        break
if isprime:
    print("prime number")  
else:
    print("not a prime number") 

#Fobanacci series
n = int(input("Enter the number:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("f{n}! = {fact}")    
n = int(input("Enter the number:"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)


#Game
moves = 34
winningpoint = int(input("Enter the winning point:"))
while moves>0:
    if moves==winningpoint:
        print("congrats!!!You Won the game")
        break
    print(f"(moves) are left.You have a chance to win the game")
    moves-1==1
else:
    print("Game over.Try again")


#
n=5
while n>0:
    print(n)
    n=n-1   #5 4 3 2 1

#
n=1
while n<7:
    print(n**2)
    n=n+1   # 1 4 9 16 25 36


#
n=int(input())
s=0
while n>0:
    s+=(n%10)
    n//=10
print(s)   #15 #6

#
n=int(input())
temp=0
rev = 0
while n>0:
    rev=rev*10+(n%10)
    n//=10
if rev==temp:
    print("Palindrome")
else:
    print("Not palindrome")


#
n=input()
full=len(n)
length=len(n)//2
ind=0
while ind<=length:
    if n[ind] !=n[full]:
        print("Not palindrome")
        break
    ind +=1
    full =-1
else:
    print('Palindrome')


