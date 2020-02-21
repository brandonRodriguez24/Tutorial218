import unittest
import math
from tutoria.OOP_Examples import bankAccount
from tutoria.OOP_Examples import version1
from tutoria.OOP_Examples import version2
from tutoria.OOP_Examples import Triangle
from tutoria.OOP_Examples import Rectangle

class MyTestCase(unittest.TestCase):
    def test_OOP_Examples_Encapsulation(self):
        account = bankAccount()
        self.assertEqual(200, account.balanceGetter())

    def test_OOP_Examples_Abstraction(self):
        self.assertEqual(4,math.sqrt(16))

    def test_OOP_Examples_Inheritance(self):
        application = version2
        self.assertEqual(application.options, "option1")

    def test_OOP_Examples_Polymorphism(self):
        objRec = Rectangle()
        objRec.perimeter(4,5,6)

if __name__ == '__main__':
    unittest.main()
