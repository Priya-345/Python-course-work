#1.Local Scope
def student():
    name = "Priyanka"
    print(name)
student()
'''output:Priyanka'''

#2.Global scope
name = "priyanka"
def student():
    print(name)
student()
print(name)
'''output:
priyanka
priyanka'''

#3.Global keyword 
name = "priyanka"
def student():
    global name
    name = "Goud"
student()
print(name)
'''output:Goud'''

def student():
    global name
    name = "priyanka"
    print('Inside:',name)

na = "Sony"
student()
print('Outside:',na)
'''Inside: Priyanka
Outside: Sony'''

def student():
    global name
    name = "priyanka"
    print('Inside:',name)

name = "Sony"
student()
print('Outside:',name)
'''Inside: priyanka
Outside: priyanka'''


#4.Enclosing Scope
def student():
    course = "python"
    print("starting course:",course)
    def change():
        nonlocal course
        course = "Java"
        print("Modified course:",course)
    change()
    print("Final Course:",course)
    print(course)
student()
'''output:
starting course: python
Modified course: Java
Final Course: Java'''

def update(a):
    a=13
    print("Inside:",a)
a=12
update(a)
print("Outside:",a)
'''output:
Inside: 13
Outside: 12'''

def update(a):
    a=a+10
    print("Inside:",a)
a=12
update(a)
print("Outside:",a)
'''output:
Inside: 22
Outside: 12'''

def update(a):
    a=a+10
    print("Inside:",a)
a=12.5
update(a)
print("Outside:",a)
'''output:
Inside: 22.5
Outside: 12.5'''

def update(a):
    a=a+"Programming"
    print("Inside:",a)
a="Python"
update(a)
print("Outside:",a)
'''output:
Inside: PythonProgramming
Outside: Python'''

def update(a):
    a=False
    print("Inside:",a)
a=True
update(a)
print("Outside:",a)
'''output:
Inside: False
Outside: True'''

def update(a):
    a=a+(4,5)
    print("Inside:",a)
a=(1,2,3)
update(a)
print("Outside:",a)
'''output:
Inside: (1, 2, 3, 4, 5)
Outside: (1, 2, 3)'''

def update(a):
    a.extend([4,5])
    print("Inside:",a)
a=[1,2,3]
update(a)
print("Outside:",a)
'''output:
Inside: [1, 2, 3, 4, 5]
Outside: [1, 2, 3, 4, 5]'''

def update(a):
    a.add(5)
    print("Inside:",a)
a={1,2,3}
update(a)
print("Outside:",a)
'''output:
Inside: {1, 2, 3, 5}
Outside: {1, 2, 3, 5}'''

def update(a):
    a.update({5:8})
    print("Inside:",a)
a={1:4,2:5,3:6}
update(a)
print("Outside:",a)
'''Inside: {1: 4, 2: 5, 3: 6, 5: 8}
Outside: {1: 4, 2: 5, 3: 6, 5: 8}'''