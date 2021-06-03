class Car:                                  #  class
    def __init__(self,name,model):        #__init__ is a constructor
        self.name = name
        self.model = model
    def display(self):
        print("car name", self.name)
        print("car model", self.model)

toyota = Car("toyota",50000)
toyota.display()
print(toyota.name)
print(toyota.model)



'''class father:                             #inheritance
    def __init__(self,car):
        self.car = car
        def display(self):
            print("fathers car is " ,self.car)

class son(father):
    pass
    def display(self) :
        print("sons car is ",self.car) 

ch=son("bmw")
ch.display()'''



'''class Father:
    def __init__(self,car):
        self.car = car
    def display (self):
        print(self.car)

class son( Father ):
    def __init__(self,car,bus,train):
        self.bus=bus
        self.train=train

        Father.__init__(self,car)
    def display(self):
        print(self.car)
        print(self.bus)
        print(self.train)


object=son("bmw","bmtc","local")
object.display()'''




'''class Csstudent:
    stream='cse'
    def __init__(self,rollno):
        self.rollno=rollno
a=Csstudent(101)
b=Csstudent(900)

print(a.stream)
print(b.stream)
print(a.rollno)
print(b.rollno)'''


#multiple inheritance
'''class Grandfather:
    def __init__(self,name):
        self.name=name
  
class Father(Grandfather):
    def __init__(self,name,height):
        self.height=height
        Grandfather.__init__(self,name)
   
class Son(Father):
    def __init__(self,name,height,age):
        self.age=age
        Father.__init__(self,name,height)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.height)            
             
s=Son("gagan",5,43)
s.display()'''


'''#multilevel inheritance
class Car:
    def __init__(self,model):
        self.model=model

class Bus:
    def __init__(self,tyre):
        self.tyre=tyre

class Van(Car,Bus):
    def __init__(self,model,tyre,company):
        self.company=company
        Car.__init__(self,model)
        Bus.__init__(self,tyre)

    def display(self):
        print(self.model)
        print(self.tyre)
        print(self.company)


a=Van(2010,"mrf","bmw")
a.display()'''
