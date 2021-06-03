#the ability to behave in different form is called method overriding or polymorphism

#----------------------------------------------------#operator overloading------------------------------------
'''class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b   
    def __add__(self,o):
        return self.a + o.b
    def pfunc(self):
        print(2+2)
ob1=A(1,3)
ob2=A(2,3)
ob3=A("x-cencia")
ob4=A("technologies")

print(ob1 + ob2)
print(ob3 + ob4)
ob2.pfunc()'''

  
#------------------------------------------special , dunder method--------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------static method--------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#------------------------------------------abstract class and method------------------------------------------
'''from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def area(self):
        return self.l*self.b
p=rectangle(10,20)
print( 'area:',p.area())'''




class obj:
    @abstractmethod
    def area(self):
        print("value")
    def fun():
        pass 

o=obj()
o.func