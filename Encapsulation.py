#You can restrict access to methods and variables.This can prevent the data from being modified by accident, is known as encapsulation
#Private method/variable can be created using  __(underscore) and can be used within that class only
# Encapsulation can be achieved by private method and private variable
# Private method and varible will be accessable by their own class

'''
class demo():
    __a=11                  #Private variable
    def display(self):
        print(self.__a)

obj=demo()
obj.display()
#print(demo.__a)             #cannot be accessed as its a private variable
'''

#Private method
'''class demo():
    def __disp1(self):      #Private method
        print('this is display1 method')

    def disp2(self):
        print('this is display2 method')
        self.__disp1()

obj=demo()
#obj.disp1()         #Not correct
obj.disp2()
'''



class speed():
    def __init__(self):
        self.speed=200              #public var
        self.__speed_limit=150       #private  var

    def get_speed(self):
        return self.speed

    def get_speed_limit(self):
        return self.__speed_limit

obj= speed()
obj.speed=100                       # publiv varibale can be changed here
obj.__speed_limit= 50               # but pvt varibale cant be modified here
print(obj.get_speed())
print(obj.get_speed_limit())