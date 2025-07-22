# 1. Positive or Negative
a = int(input("Enter a number :  "))
if a>0:
    print("Positive")
else :
    print("Negative")

# 2. Even or Odd
n = int(input("Enter a integer : "))
if n%2==0 :
    print(" The number is Even")
else :
    print(" The number is odd")

# 3. Divisible by 5
number = int(input("Enter a number: "))
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")

# 4. Divisible by 3 and 7
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 7 == 0:
    print(f"{number} is divisible by both 3 and 7.")
else:
    print(f"{number} is not divisible by both 3 and 7.")

# 5. Check for Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 6. Check Pass or Fail (Passing marks = 35)
marks = int(input("Enter your marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

#7. Check if number is 3-digit
number = int(input("Enter a number: "))
if 100 <= abs(number) <= 999:
    print(f"{number} is a 3-digit number.")
else:
    print(f"{number} is not a 3-digit number.")

#8. Check if character is vowel
char = input("Enter a single character: ").lower()
if char in ['a', 'e', 'i', 'o', 'u']:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")

#9. Check greatest of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print("Both numbers are equal.")

#10. Check smallest of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 < num2:
    print(f"{num1} is smaller than {num2}.")
elif num2 < num1:
    print(f"{num2} is smaller than {num1}.")
else:
    print("Both numbers are equal.")

# 11.Check if number is zero
number = float(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
else:
    print("The number is not zero.")

# 12.Check if number is multiple of 10
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

# 13.Check if age is eligible to vote (18+)
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# 14. Check if number is between 1 and 100
number = int(input("Enter a number: "))
if 1 <= number <= 100:
    print(f"{number} is between 1 and 100.")
else:
    print(f"{number} is not between 1 and 100.")

#15. Check if number is square of another
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 ** 2 == num2:
    print(f"{num2} is the square of {num1}.")
elif num2 ** 2 == num1:
    print(f"{num1} is the square of {num2}.")
else:
    print("Neither number is the square of the other.")

#16. Check if two strings are equal
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

# 17. Check if a number is prime (basic logic)
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# 18. Check if number is positive and even
number = int(input("Enter a number: "))
if number > 0 and number % 2 == 0:
    print(f"{number} is positive and even.")
else:
    print(f"{number} is not both positive and even.")

# 19. Check if character is uppercase
char = input("Enter a single character: ")
if len(char) == 1 and char.isalpha():
    if char.isupper():
        print(f"{char} is an uppercase letter.")
    else:
        print(f"{char} is not an uppercase letter.")
else:
    print("Please enter a single alphabetic character.")

# 20. Check if temperature is hot (>30°C)
temperature = float(input("Enter the temperature in °C: "))
if temperature > 30:
    print("It's hot.")
else:
    print("It's not hot.")


#
#
#1. Check if a number is a 4-digit even number
number = int(input("Enter a number: "))
if 1000 <= abs(number) <= 9999 and number % 2 == 0:
    print(f"{number} is a 4-digit even number.")
else:
    print(f"{number} is not a 4-digit even number.")

#2. Check if a character is a consonant
char = input("Enter a single character: ").lower()
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"{char} is a vowel, not a consonant.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Please enter a single alphabetic character.")

#3. Check if a number is divisible by 2 or 3 but not both
number = int(input("Enter a number: "))
if (number % 2 == 0) ^ (number % 3 == 0):  # XOR logic
    print(f"{number} is divisible by 2 or 3, but not both.")
else:
    print(f"{number} is either divisible by both or by neither.")

#4. Check if a number is negative and odd
number = int(input("Enter a number: "))
if number < 0 and number % 2 != 0:
    print(f"{number} is negative and odd.")
else:
    print(f"{number} is not both negative and odd.")

#5. Check if a string starts with a vowel
text = input("Enter a string: ")
if text and text[0].lower() in 'aeiou':
    print(f"The string starts with a vowel: '{text[0]}'")
else:
    print("The string does not start with a vowel.")

#6. Check if three sides form a valid triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a + b > c and a + c > b and b + c > a:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")

#7. Find the greatest among three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
print(f"The greatest number is {greatest}.")

#8. Check if a year is a century year and leap year
year = int(input("Enter a year: "))
if year % 100 == 0:
    print(f"{year} is a century year.")
    if year % 400 == 0:
        print(f"{year} is also a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a century year.")
    
    # For non-century years, check leap year as usual
    if (year % 4 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

#9. Check if a character is a digit
char = input("Enter a single character: ")
if len(char) == 1 and char.isdigit():
    print(f"'{char}' is a digit.")
else:
    print(f"'{char}' is not a digit.")

#10. Check if a number is palindrome (integer)
num = int(input("Enter an integer: "))
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

#11. Compare lengths of two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) > len(str2):
    print("The first string is longer.")
elif len(str1) < len(str2):
    print("The second string is longer.")
else:
    print("Both strings have the same length.")

#12. Check if a number is within a specific range (50 to 100) and divisible by 5
number = int(input("Enter a number: "))
if 50 <= number <= 100 and number % 5 == 0:
    print(f"{number} is within the range 50 to 100 and divisible by 5.")
else:
    print(f"{number} does not meet the criteria.")

#13. Validate if a password length is strong (8 or more characters)
password = input("Enter your password: ")
if len(password) >= 8:
    print("Password length is strong.")
else:
    print("Password length is weak. It should be at least 8 characters.")

#14. Check if sum of two numbers is even
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
if total % 2 == 0:
    print(f"The sum {total} is even.")
else:
    print(f"The sum {total} is odd.")

#15. Check if the character is a special symbol (!, @, #, etc.)
special_symbols = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")
char = input("Enter a single character: ")
if len(char) == 1:
    if char in special_symbols:
        print(f"'{char}' is a special symbol.")
    else:
        print(f"'{char}' is not a special symbol.")
else:
    print("Please enter exactly one character.")

#16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)
temperature = float(input("Enter the temperature in °C: "))
if temperature < 15:
    print("The temperature is cold.")
elif 15 <= temperature <= 30:
    print("The temperature is moderate.")
else:
    print("The temperature is hot.")

#17. Check if a number lies outside the range 10 to 50
number = int(input("Enter a number: "))
if number < 10 or number > 50:
    print(f"{number} lies outside the range 10 to 50.")
else:
    print(f"{number} lies within the range 10 to 50.")

#18. Check if number is a perfect square (basic method)
number = int(input("Enter a number: "))
if number < 0:
    print(f"{number} is not a perfect square (negative number).")
else:
    root = int(number ** 0.5)
    if root * root == number:
        print(f"{number} is a perfect square.")
    else:
        print(f"{number} is not a perfect square.")

#19. Compare two ages and determine who is older or if same age
age1 = int(input("Enter first age: "))
age2 = int(input("Enter second age: "))
if age1 > age2:
    print("The first person is older.")
elif age2 > age1:
    print("The second person is older.")
else:
    print("Both persons are of the same age.")

#20. Check if an angle is acute, right, or obtuse
angle = float(input("Enter the angle in degrees: "))
if angle > 0 and angle < 90:
    print("The angle is acute.")
elif angle == 90:
    print("The angle is right.")
elif angle > 90 and angle < 180:
    print("The angle is obtuse.")
else:
    print("Invalid angle. Please enter an angle between 0 and 180 degrees.")



