def AreaOfCircle():
    print('''
          Program:
          ---------
          radius = float(input("Enter the radius: "))
          area = 3.1416 * radius * radius
          print("Area of the circle is:", area)
          
          Test Cases:
          -----------
          Input: 5
          Output: Area of the circle with radius 5 is: 78.54

          Input: -3
          Output: Error: Radius cannot be negative
          
          Explanation:
          The formula used is: Area=3.1416×radius2
          ''' )


def CheckAge():
    print('''
         Program:
         ------------
         age = int(input("Enter your age: "))
         if age >= 18:
            print("You are an adult (18+).")
         else:
            print("You are under 18.")


        Test Cases:
        ----------------
        Input :  17
        Output : You are under 18.

        Input :  18
        Output : You are an adult(18+).

        Explanation :
       --------------------
        The program checks if age is 18 or more

        ''')


def SimpleInterest():
      print('''
         Program:
         ---------------
         P = float(input("Enter the principal amount: "))
         R = float(input("Enter the rate of interest: "))
         T = float(input("Enter the time (in years): "))

         SI = (P * R * T) / 100
         print("Simple Interest is:", SI)

         Test Cases:
         ----------------
         Input: principal amount: 1000,rate of interest: 5,time (in years): 2
         
         Output:
         Simple Interest is: 100.0

        Explanation :
        --------------------
        The formula (P * R * T) / 100 is used to calculate simple interest.
        ''')

def DiamondPattern():
     print('''
         Program:
         ---------------
         n = 5
         for i in range(n):
         print(' ' * (n - i - 1) + '* ' * (i + 1))
         for i in range(n - 2, -1, -1):
         print(' ' * (n - i - 1) + '* ' * (i + 1))


         Test Cases:
         ----------------
         Input:   n = 5
         Output:
                 *    
                ***   
               *****  
              ******* 
             *********
              ******* 
               *****  
                ***   
                 *

        Explanation :
        --------------------
        n is the number of rows for half the diamond.
        Upper half goes from 1 to n, printing increasing stars.
        Lower half goes from n-1 to 1, printing decreasing stars.
        Formula for stars: 2 * i - 1
        Formula for spaces: n - i
                  
       ''')


def CountVowels():
    print('''
         Program:
         ---------------
         def count_vowels(text):
         vowels = "aeiouAEIOU"
         count = 0
         for char in text:
            if char in vowels:
                count += 1
         return count
         input_string = input("Enter a string: ")
         print("Number of vowels:", count_vowels(input_string))


         Test Cases:
         ----------------
         Input: "hello"
         Output: 2
        
         Input: "bcdfg"
         Output: 0

         Explanation :
         --------------------
         It counts the vowelsin the string

         ''')




def Divisible():
     print('''
         Program:
         ---------------
         number = int(input("Enter a number: "))
         if number % 3 == 0 and number % 7 == 0:
             print("The number is divisible by both 3 and 7.")
         else:
             print("The number is NOT divisible by both 3 and 7.")


         Test Cases:
         ----------------
         
         Input : 21
         Output : The number is divisible by both 3 and 7.

         Input : 14
         Output : The number is not  divisible by both 3 and 7.


        Explanation :
        --------------------
        % is the modulus operator — it gives the remainder.
        Using and checks both conditions.
        If both are true, print the result.

        ''')



def CheckPassOrFail():
     print('''
         Program:
         ---------------
         marks = int(input("Enter your marks: "))
         if marks >= 40:
            print("Pass")
         else:
            print("Fail")


         Test Cases:
         ----------------
         Input  : 75
         Output : Pass

         Input  : 25
         Output : Fail

         Explanation :
         --------------------
         The user is asked to input their marks.
         If the marks are 40 or more, the program prints "Pass".
         If the marks are less than 40, it prints "Fail".

         ''')



def CheckString():
     print('''
         Program:
         ---------------
         str1 = input("Enter first string: ")
         str2 = input("Enter second string: ")
         if str1 == str2:
             print("Strings are equal")
         else:
             print("Strings are not equal")



          Test Cases:
          ----------------
          Input 1 : "apple"
          Input 2 : "apple"
          Output  : Strings are equal


          Input 1 : "Apple"
          Input 2 : "apple"
          Output  : Strings are not equal


          Explanation :
          --------------------
         The program takes two strings as input from the user.
         If they are equal, it prints "Strings are equal".
         Otherwise, it prints "Strings are not equal".


         ''')



def Temperature():
    print('''
         Program:
         ---------------
         temperature = float(input("Enter the temperature in Celsius: "))
         if temperature >= 35:
             print("It's hot")
         else:
             print("It's not hot")


         Test Cases:
         ----------------
         Input  : 40
         Output : It's hot


         Input  : 20
         Output : It's  not hot


          Explanation :
          --------------------
          It checks if the temperature is greater than or equal to 35


          ''')



def PrefectSquare():
    print('''
         Program:
         ---------------
         import math
         def is_perfect_square(num):
             if num < 0:
                return False 
             sqrt = math.sqrt(num)
             return sqrt == int(sqrt)
         number = int(input("Enter a number: "))
         if is_perfect_square(number):
             print("Perfect square")
         else:
             print("Not a perfect square")



         Test Cases:
         ----------------
         Input  : 49
         Output : Perfect square


         Input  : 18
         Output : Not a Perfect square


         Explanation :
         --------------------
         calculates the square root using math.sqrt().


         ''')
    