# class name should be in capital
# class Test:
#     a = 10  # attribute
#     b = 11
#     sum = a + b

#     def test_function(self):
#         print(self.sum)

#     def test_1(self):
#         print(self.a)

#     def test_2(self):
#         print(self.b)


# obj = Test()
# # obj.(test_1 + test_2)
# obj.test_function()


# # print(obj.a)
# # print(obj.sum)
# class Test1:
#     a = 10

#     def __str__(self) -> str:
#         return f"the value of num1is {self.a}"

#     def test_function(self):
#         return "this is function"


# obj = Test1()
# print(obj)


# class constructor
# class Test2:
#     def __init__(self, a, b):

#         # self.num1= 10
#         # self.num2 = 12
#         # by using arguments
#         self.num1 = a
#         self.num2 = b

#     def add(self):
#         return self.num1 + self.num2

#     def mul(self):
#         return self.add() * 2


# obj = Test2(4, 6)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())


# inheritance class
# class ParentA:
#     a = 10
#     b = 12


# class ParentB(ParentA):
#     c = 11


# obj = ParentB
# print(obj.a)


# string
# from typing import Any


# class Alfa:
#     def __init__(self, name) -> None:
#         self.name = name

#     def names(self):
#         return self.name

#     def full_name(self):
#         return f"{self.name} rawal"


# data = input("Enter the name ")
# obj = Alfa(data)



# inheritance
class Beta:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname


class Gama(Beta):
    def l_name(self):
       txt = self.firstname 
       tyt = self.lastname 
       return f'{txt} {tyt}'


obj = Gama("utsab","maharjan")
print(obj.l_name())
