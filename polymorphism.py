# class A:
#     def new(self,a,b):
#         return a+b
#     def new(self,x,y,z):
#         return x+y+z

# obj=A()
# print(obj.new(5,6,7))
# print(obj.new(5,6))  
#  
#=====================================

# class A:
    
#     def new(self,x=0,y=0,z=0):
#         return x+y+z

# obj=A()
# print(obj.new(50,60,70))
# print(obj.new(50,60))   
# print(obj.new(50))   
# print(obj.new())   
#======================================
from multipledispatch import dispatch

# class A:
#     # @dispatch (int,int)
#     def add (self,x,y,):
#         print (x,y)
#     # @dispatch (int,int,int)
#     def add (self,x,y,z):
#         print (x,y,z)

# obj =A()
# obj.add(23,15)
# obj.add(23,15,16)

#====================================
class A:
    def add(self,a,b):
        print("from parent class")
        return a+b
class B(A):
    def add(self,x,y):
        print("from child class")
        return x+y
    
obj =B()
obj.add(5,6)    

























