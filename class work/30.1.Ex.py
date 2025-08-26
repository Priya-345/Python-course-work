#
class Numbers:
    def _init_(self,number):
        self.number=number
    def _add_(self,other):
        return self.number+other.number
    def _sub_(self,other):
        return self.number-other.number
    def _mul_(self,other):
        return self.number*other.number
    def _truediv_(self,other):
        return self.number/other.number
    def _gt_(self,other):
        return self.number>other.number
    def _lt_(self,other):
        return self.number<other.number
    def _eq_(self,other):
        return self.number==other.number
    def _str_(self):
        return f'{self.number}'
    
n1=Numbers(20)
n2=Numbers(10)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1>n2)
print(n1<n2)
print(n1==n2)


        