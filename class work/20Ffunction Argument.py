 #1.Positional Agr
def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")

student_details(name,rollno,marks,grade,student_course)
student_details("xyz",65,100,'A','Java')

 # 2.Keyword Agr
def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")
student_details(name=name,rollno=rollno,marks=marks,grade=grade,course=student_course)
student_details(rollno=rollno,name=name,grade=grade,course=student_course,marks=marks)
student_details(rollno=56,name='ramya',grade='A',course='Mysql',marks=99)

# 3.Default Agr
def student_details(name,rollno,marks=0,grade="F",course='Python'):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
course=input("Course: ")

student_details(name,rollno)
student_details(name,rollno,marks)
student_details(name,rollno,marks,grade)
student_details(name,rollno,marks,grade,course)

# 4.Variable Lenght
def names(*stdnames):
    print("\nName of students")
    for i in stdnames:
        print(f"**{i.upper()}**")

names('kalyan','Adarsh','saikumar')
names('kalyan','Adarsh','saikumar','nihitha','keethana','leorah')
names('kalyan','nihitha','keethana','leorah')
names('Ramya','nihitha','keethana','leorah')
names('Ramya','nihitha','keethana','Sunitha','maheswari')

# example
def display_products(**product):
    print("\nProducts and Prices: ")
    for i in product:
        print(f'{i}: ${product[i]}')

display_products(laptop=60000,phone=35000,watch=15000,fridge=200000)
display_products(fashwash=600,perfume=2000,eyeliner=1500,powder=2500)
display_products(carrot=25,tomato=30,beetroot=40,apple=50)
