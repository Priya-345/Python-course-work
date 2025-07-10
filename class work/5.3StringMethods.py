#String Methods

#1.Case Conversion Methods
# Uppercase
text = "hello"
print(text.upper()) #HELLO

# Lowercase
text = "HELLO"
print(text.lower()) #hello

# Capitalize
text1 = "python program"
print(text1.capitalize()) #Python program

# Title
print(text1.title()) #Python Program

# Swapcase
print(text1.swapcase()) #PYTHON PROGRAM

#2.Alignment & Formatting
# Center width
text2 = "python"
print(text2.center(22,"*")) #********python********

# Left-align
text3 = "python"
print(text3.ljust(18,"*")) #python************

# Right-align
text4 = "python"
print(text4.rjust(14,"*")) #********python

# Pads the string with zero on the left
text5 = "40"
print(text5.zfill(8)) #00000040

#3.Search & Find Methods
# Index of first occurrence
text6 = "python"
print(text6.find("o")) #4
print(text6.find("p")) #0

# Last Occurrence
text7 = "Hello"
print(text7.rfind("e")) #1
print(text7.find("l"))  #2

# Find error not found
S = "hello"
print(S.index("l")) #2

# rfind
print(S.rindex("e")) #1

# count
text8  = "Apple"
print(text8.count("p")) #2
print(text8.count("e")) #1 

#4.String Testing Methods
#startswith
s = "python"
print(s.startswith("pyt")) #True
print(s.startswith("on")) #False

#endswith
print(s.endswith("hon")) #True
print(s.endswith("py"))  #False

#isalpha()
S = "Hello"
print(S.isalpha()) #True
S = "Hello12"
print(S.isalpha()) #False

#isalnum()
s = "abc123"
print(s.isalnum()) #True

#islower()
s = "python"
print(s.islower()) #True

#isupper()
s = "HELLO"
print(s.isupper()) #True

#isspace()
s = "    python"
print(s.isspace()) #False
s = "      "
print(s.isspace())  #True

#istitle()
S = "Hello World"
print(S.istitle()) #True

#isidentifier()
S = "variable1"
print(S.isidentifier()) #True

#5. Replace & Modify Methods
#replace(old,new)
string = "python is programming language"
print(string.replace("is","are")) #python are programming language

#translate(table)
txt = "Hello Sam"
mytable = str.maketrans("S","P")
print(txt.translate(mytable)) #Hello Pam

#maketrans()
s = "python"
print("s".maketrans("aon","%#5")) #{97: 37, 111: 35, 110: 53}

#6. Splitting & Joining Methods
#split(sep)
s = "a,b,c"
print(s.split(",")) #['a', 'b', 'c']

#rsplit(sep)
print(s.rsplit(",", 1)) #['a,b', 'c']

#splitlines()
S = "Hello\nWorld"
print(S.splitlines()) #['Hello', 'World']

#join(iterable)
print("".join(["Hello", "World"])) #HelloWorld

#partition(sep)
S = "Hello-World"
print(S.partition("-")) #('Hello', '-', 'World')

#rpartition(sep)
S = "Hello-World-program"
print(S.rpartition("-")) #('Hello-World', '-', 'program')

#7. Whitespace & Trimming Methods
#strip(chars)
S = "     hello"
print(S.strip()) #hello

#lstrip(chars)
S = "-------hello"
print(S.lstrip("-")) #hello

#rstrip(chars)
S = "hello------" 
print(S.strip("-")) #hello

#8. Encoding & Decoding Methods
#encode(encoding)
s = "hello"
print(s.encode("utf-8")) #b'hello'

#decode(encoding)
s = b'hello'
print(s.decode("utf-8")) #hello