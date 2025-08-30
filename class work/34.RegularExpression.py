#
import re
pattern=r'Hello'
res=re.match(pattern,'Hello world')
print(res.group() if res else 'No match')         #Hello

#
import re
pattern=r'[aeiou]'
res=re.match(pattern,'Hello world')
print(res.group() if res else 'No match')       #No match

#
import re
pattern=r'\d'
res=re.match(pattern,'18hello world')
print(res.group() if res else 'No match')     #1

# search pattern
import re
pattern=r'[aeiou]'
res=re.search(pattern,'hello world18')
print(res.group() if res else 'No match')      #e

#findall
import re
pattern=r'[aeiou]'
res=re.findall(pattern,'hello world18')
#print(res.group() if res else 'No match')
print(res)                                      #['e', 'o', 'o']

#
import re
pattern=r'\d{4}|\d{2}'
res=re.findall(pattern,'pfs-31 2025 pfs-14 2024 pfs-10 2023')
print(res)                                      #['31', '2025', '14', '2024', '10', '2023']

#finditer
import re
pattern=r'\d{4}|\d{2}'
res=re.finditer(pattern,'pfs-31 2025 pfs-14 2024 pfs-10 2023')
for i in res:
    print(i.group(),i.start())

'''
31 4
2025 7
14 16
2024 19
10 28
2023 31'''

#fullmatch
import re
pattern=r'\d{10}'
res=re.fullmatch(pattern,'2024200323')
print(res.group() if res else 'No match')          #2024200323

#sub
import re
pattern=r'[A-Z]'
res=re.sub(pattern,'@','Python Programming language')
print(res)                                            #@ython @rogramming language


import re
pattern=r'[aeiou]'
res=re.sub(pattern,'*','Python Programming language')
print(res)                                             #Pyth*n Pr*gr*mm*ng l*ng**g*

#split
import re
pattern=r'[:,0]'
res=re.split(pattern,'pvhjh:oxchyrv,ghhscnmj0gvjhkl')
print(res)                                              #['pvhjh', 'oxchyrv', 'ghhscnmj', 'gvjhkl']

#
import re
pattern=r'.ood'
res=re.findall(pattern,'hot hit hat hood wood food good')
print(res)                                            #['hood', 'wood', 'food', 'good']


#
import re
pattern=r'(aeiou\d{3})'
res=re.findall(pattern,'aeiou459')
print(res)                                        #['aeiou459']


import re
pattern=r'\bho\b'
res=re.findall(pattern,'ho hoo hooh hoo')
print(res)                                        #['aeiou459']
