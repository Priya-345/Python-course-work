##
class Driver:
    def display(self,name,gender,vehno,vehtype):
        self.name=name
        self.gender=gender
        self.vehno=vehno
        self.vehtype=vehtype
        print("Driver Details: ")
        print(self.name)
        print(self.gender)
        print(self.vehno)
        print(self.vehtype)
class FareCal(Driver):
    def display(self,name,gender,vehno,vehtype):
        super().display(name,gender,vehno,vehtype)
        print("2-Wheels  -60")
        print("3-Wheels  -90")
        print("4-Wheels  -120")
a=FareCal()
a.display('abc','F','A123','3')
'''
Driver Details: 
abc
F
A123
3
2-Wheels  -60
3-Wheels  -90
4-Wheels  -120'''

#   
class A:
    def print_(self):
        print("This the parent class->A")
class B(A):
    def print_(self):
        super().print_()
        print("This the child class-B")
class C(B):
    def print_(self):
        super().print_()
        print("This the grand class-C")
c=C()
c.print_()

'''This the parent class->A
This the child class-B
This the grand class-C'''

#
class A:
    def print_(self):
        print("This the parent class-A")
class B:
    def print_(self):
        print("This the child class-B")
class C(A,B):
    def print_(self):
        A.print_(self)
        B.print_(self)
        print("This the grand class-C")
c=C()
c.print_()
