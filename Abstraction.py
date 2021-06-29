# A class derived from ABC class which belongs to abc module, is known as abstract class in python
#Abstract classes are classes that contains one or more abstarct methods. abstract method is a method that is declared but contains no implementation
# This is used when requirement is clear but design is not clear, Later part we can keep on adding on that classes
# ABC is predefined abstract class in python

#We cannot call abstarct class using object, we need to creat a child class and define the abstract method

from abc import ABC, abstractmethod

class father(ABC):              #abstract class

    @abstractmethod
    def disp(self):             #abstract mrthod
        pass

    def show(self):
        print('concrete method')

class child(father):
    def disp(self):             #call abstarct method in child class
        print('calling avstract method')

c=child()
c.disp()
c.show()
print('********************************************')

#Ex2

from abc import ABC, abstractmethod

class defense(ABC):

    def area(self):
        pass

    def weapon(self):
        print('Gun= AK47')

class army(defense):
    def area(self):
        print('area= land')

class airforce(defense):
    def area(self):
        print('area= sky')

class navy(defense):
    def area(self):
        print('area= sea')

obj= army()
obj.area()
obj.weapon()

obj1=airforce()
obj1.area()
obj.weapon()

obj2=navy()
obj2.area()
obj.weapon()