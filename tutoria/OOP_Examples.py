#Brandon Rodriguez UCID:31429741

#Encapsulation
class bankAccount():
    def __init__(self, accountBalance=200):
        self.__accountBalance=accountBalance

    def balanceGetter(self):
        print(self.__accountBalance)
    def balanceSetter_withdraw(self,value):
        self.__accountBalance=self.__accountBalance - value

account = bankAccount()

account.balanceGetter()
account.balanceSetter_withdraw(50)

#Abstraction
import math
math.sqrt(16)

#Inheritance
class version1:
    def options(self):
        print("option1")

class version2(version1):
    def listOptions(self):
        print("here are your options")

if __name__=='__main__':
    application = version2()
    application.listOptions()
    application.options()

#Polymorphism
class Triangle():
    def perimeter(self,a,b,c):
        print(a + b + c)
class Rectangle():
    def perimeter(self,a,b):
        print(2*(a+b))
objTri = Triangle()
objRec = Rectangle()
for shape in (objRec, objTri):
    shape.perimeter(4,5,6)
