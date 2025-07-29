#Nested Loops

# ex 1
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print('*',end='')
    print()

'''Output
*****
*****
*****
*****
*****'''

# ex2
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(row,end='')
    print()

''' output
000000
111111
222222
333333
444444
555555'''

# ex 3
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(col,end='')
    print()

''' output
01234567
01234567
01234567
01234567
01234567
01234567
01234567
01234567'''


# ex 4
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(row+1):
        print('*',end='')
    print()

'''output
*
**
***
****
*****
******'''

# ex 5
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row):
        print('*',end='')
    print()

'''output
******
*****
****
***
**
*    '''

# ex 6
n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()

    '''output      
            * 
          * *
        * * *
      * * * *
    * * * * *
  * * * * * *
* * * * * * *'''

# ex 7
n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()

'''output
* * * * * * 
  * * * * *
    * * * *
      * * *
        * *
          *'''

# ex 8
n=int(input("Enter the size:"))
for row in range(n):
    if row<=n//2:
       for col1 in range(row+1):
           print('*',end=' ')
    else:
        for col2 in range(n-row):
             print('*',end=' ')
    print()

'''output
* 
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*'''

# ex 9
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0  or row==n-1 or col==n-1:
           print('*',end=' ')
        else:
          print(' ',end=' ')
    print()

'''output
* * * * * * * * * * * * * 
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
* * * * * * * * * * * * *'''

# ex 10
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0  or row==n-1 or col==n-1 or row==n//2 :
           print('*',end=' ')
        else:
          print(' ',end=' ')
    print()


'''output
* * * * * * * * * * * * 
*                     *
*                     *
*                     *
*                     *
*                     *
* * * * * * * * * * * *
*                     *
*                     *
*                     *
*                     *
* * * * * * * * * * * *'''

# ex 11
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0  or row==n-1 or col==n-1 or row==n//2 or  col==n//2 :
           print('*',end=' ')
        else:
           print(' ',end=' ')
    print()
'''
* * * * * * * * * * * * * * * * * * * * * * * 
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
* * * * * * * * * * * * * * * * * * * * * * *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
*                     *                     *
* * * * * * * * * * * * * * * * * * * * * * * '''


# ex 12
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''output
* * * * * * * * * * * * * * * * * * 
                                *
                              *
                            *
                          *
                        *
                      *
                    *
                  *
                *
              *
            *
          *
        *
      *
    *
  *
* * * * * * * * * * * * * * * * * *'''

# ex 13
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        if col==row or col+row==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''output
*                           * 
  *                       *
    *                   *
      *               *
        *           *
          *       *
            *   *
              *
            *   *
          *       *
        *           *
      *               *
    *                   *
  *                       *
*                           *'''

