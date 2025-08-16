from Programs import *
Programs={
    1:{'name' : 'Area Of Circle'},
    2:{'name' : 'Check Age'},
    3:{'name' : 'Simple Interset'},
    4:{'name' : 'Diamond Pattern'},
    5:{'name' : 'Count Vowels in a string'},
    6:{'name' : 'Divisible by 3 and 7'},
    7:{'name' : 'Check Pass or Fail'},
    8:{'name' : 'Check to strings are equal'},
    9:{'name' : 'check if temperature is hot'},
    10:{'name' : 'check if a number is perfect square'}
    }
for i in Programs:
     print(f'{i}.{Programs[i]["name"]}')


while True:
    ch=int(input("Enter the choice[0-Exit]:  "))
    if ch==1:
        AreaOfCircle()
    elif ch==2:
        CheckAge()
    elif ch==3:
        SimpleInterest()
    elif ch==4:
        DiamondPattern()
    elif ch==5:
        CountVowels()
    elif ch==6:
        Divisible()
    elif ch==7:
        CheckPassOrFail() 
    elif ch==8:
        CheckString()
    elif ch==9:
        Temperature()
    elif ch==10:
        Temperature()
    elif ch==0:
        break
    else:
        print("Invalid Choice")