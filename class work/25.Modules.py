##
#import sys
#print(sys.argv)
#print(sys.version)

##
import sys
print("Before exit")
print(sys.exit())
print("After exit")
''' Before exit'''

##
import platform
print(platform.system())
print(platform.release())
print(platform.processor())
'''Windows
10'''

##
import math
print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.pow(3,3))
'''
3.141592653589793
2.718281828459045
5.0
27.0'''

'''print(round(12.3))
print(round(12.8))
12
13'''

import math
print(math.ceil(12.3))
print(math.ceil(12.8))
print(math.ceil(12.000001))
print(math.floor(12.3))
print(math.floor(12.8))
print(math.floor(12.99999999))


print(abs(-13))
print(abs(-12.4))

print(math.fabs(-13))
print(math.factorial(5))
print(math.gcd(8,12))

print(math.log(2))
print(math.log(2,2))
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print(math.degrees(45))
print(math.radians(45))

'''
13
13
13
12
12
12
13
12.4
13.0
120
4
0.6931471805599453
1.0
0.8509035245341184
0.5253219888177297
1.6197751905438615
2578.3100780887044
0.7853981633974483   '''


##
import random
random.seed(10)
print(random.random())
print(random.randint(1,10))
print(random.uniform(1,5))
l=['afrin','keerthana','revathi','priyanka']
print(random.choice(l))
print(random.choices(l,k=2))
print(l)
print(random.shuffle(l))
print(l)

'''
0.5714025946899135
7
2.9302466982034234
afrin
['afrin', 'priyanka']
['afrin', 'keerthana', 'revathi', 'priyanka']
None
['keerthana', 'afrin', 'priyanka', 'revathi']'''

## Itertools
from itertools import combinations,permutations
s='abc'
t=tuple(combinations(s,3))
p=tuple(permutations(s,3))
for i in t:
    print(''.join(i),end=',')
print()
for i in p:
    print(''.join(i),end=',') 
    
'''abc,
abc,acb,bac,bca,cab,cba,'''


from collections import deque,defaultdict,Counter
s=[1,2,3,2,4,5,4,5,6,7,4,3,2,1,3,4,5,6,5,6,7,3]
feq=Counter(s)
print(feq)
'''Counter({3: 4, 4: 4, 5: 4, 2: 3, 6: 3, 1: 2, 7: 2}) '''


from collections import deque,defaultdict,Counter
s=[1,2,3,4,1,2,3,6,1,2,3,6,1,7,2,3,4,5]
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
'''defaultdict(<class 'int'>, {1: 4, 2: 4, 3: 4, 4: 2, 6: 2, 7: 1, 5: 1})'''

from collections import deque,defaultdict,Counter
d=deque()
d.appendleft(12)
d.pop()

d.append(12)
d.popleft()
print(d)
'''
12345678
    --------------------
in                         out
    --------------------
    
    --------------------
out 
    --------------------'''

#deque([])


#Date and Time

from datetime import date,time,datetime,timedelta
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

print(date(2001,12,4))
print(time(12,30,44))

now=datetime.now()
print(now)
print(now.year)
print(now.day)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)

print(now.strftime('%y-%m-%d'))
print(now.strftime('%d/%m/%Y'))
print(now.strftime('%d/%m/%Y %H:%M:%S'))
print(now.strftime('%b %d, %Y %H:%M:%S'))
print(now.strftime('%B %d, %Y %H:%M:%S'))
print(now.strftime('%B %d, %Y %H:%M:%S %p'))
print(now.strftime('%a, %B %d, %Y %H:%M:%S %p'))
print(now.strftime('%A, %B %d, %Y %H:%M:%S %p'))
print(now.strftime('%A, %B %d, %Y %I:%M:%S %p'))

future=today-timedelta(weeks=10)
futureday=today-timedelta(days=10)
futuretime=now+timedelta(minutes=30)
futurehour=now+timedelta(hours=3)

print(future,futureday,futuretime,futurehour.strftime('%A, %B %d, %Y %I:%M:%S %p'))

'''
deque([])
2025-08-13
2025      
8
13        
2
3
2001-12-04
12:30:44
2025-08-13 14:57:00.792425
2025
13
8
14
57
0
25-08-13
13/08/2025
13/08/2025 14:57:00
Aug 13, 2025 14:57:00
August 13, 2025 14:57:00
August 13, 2025 14:57:00 PM
Wed, August 13, 2025 14:57:00 PM
Wednesday, August 13, 2025 14:57:00 PM
Wednesday, August 13, 2025 02:57:00 PM
2025-06-04 2025-08-03 2025-08-13 15:27:00.792425 Wednesday, August 13, 2025 05:57:00 PM  '''
