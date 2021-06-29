#polymorphism is the condition of occurrence in different forms. it uses two method overRiding & overLoading
# Overriding means having two method with same name but doing different tasks, it means one method overrides the other
#Methd overriding is used when programmer want to modify the existing behavior of a method

#Overriding

class Add:
    def result(self,x,y):
        print('addition', x+y)

class mult(Add):
    def result(self,x,y):
        print('multiplication', x*y)

obj= mult()
obj.result(5,6)

#Using superclass method we can modify the parent class method and call it in child class

class Add:
    def result(self,x,y):
        print('addition', x+y)

class mult(Add):
    def result(self,a,b):
        super().result(10,11)
        print('multiplication', a*b)

obj= mult()
obj.result(10,20)

#Overloading: we can define a method in such a way that it can be called in different ways
class intro():
    def greeting(self,name=None):
        if name is not  None:
            print('Hello ', name)
        if name is None:
            print('no input given')
        else:
            print('Hello Alien')

obj1= intro()
obj1.greeting('Umasankar')
obj1.greeting(None)

#Ex2
class calculator:
    def number(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!= None:
            s=a+b
        else:
            s= 'enter atlest two number'
        return s

ob=calculator()
print(ob.number(10,))