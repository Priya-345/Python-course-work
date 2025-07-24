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
full=len(n)-1
length=len(n)//2
ind=0
while ind<=length:
    if n[ind]!=n[full]:
        print("Not palindrome")
        break
    ind+=1
    full=-1
else:
    print('Palindrome')