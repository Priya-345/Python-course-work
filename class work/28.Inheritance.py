##

class A:
    def printa(self):
        print("This is the parent class")
a=A()
a.printa()      #This is the parent class

# single inheritance
class A:
    def printa(self):
        print("This is the parent class-A")

class B(A):
    def printb(self):
        print("This is child class-B->A")
 
b=B()
b.printa()
b.printb()   
#This is the parent class-A        
#This is child class-B->A

# multilevel inheritance
class A:
    def printa(self):
        print("This is the parent class: A")

class B(A):
    def printb(self):
        print("This is child class: B->A")
class C(B):
    def printc(self):
        print("This is  grand child class: C-B->A") 
c=C()
c.printa()
c.printb()
c.printc()

#This is the parent class: A       
#This is child class: B->A
#This is  grand child class: C-B->A


# Hierarchical Inheritance
class A:
    def printa(self):
        print("This is the parent class: A->(A,B,D)")

class B(A):
    def printb(self):
        print("This is child class: B->A")
class C(A):
    def printc(self):
        print("This is child class: C->A") 
class D(A):
    def printd(self):
        print('This is the child class: D->A')

d=D()
d.printa()
d.printd()

#This is the parent class: A->(A,B,D)
#This is the child class: D->A   


