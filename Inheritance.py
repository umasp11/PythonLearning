#Classes can inherit the function of other classes
#If an object is creted usng a class that inhrits from a suprclass, the objct will contin the mthod of both the class & superClass

"""Method Resolution Order (MRO)
it is the order in which Python looks for a method in a hierarchy of classes.
Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes.

Parent/base/super class -> child/sub/derived
"""

'''class A:                        #Parent class
    def m1(self):
        print('this is from Class A')

class B(A):                     #Child class
    def m2(self):
        print('this is from Class B')

obja = A()                          #Parent object
obja.m1()

objb= B()                           #Child object
objb.m1()
objb.m2()
'''

#Multilevel inhertance
'''
class A:
    a,b=10,20               #Parent class
    def m1(self):
        print(self.a+self.b)

class B(A):
    m,n=50,60               #Child class
    def m2(self):
        print(self.m+self.n)

class C(B):
    x,y=90,110              #Child class
    def m3(self):
        print(self.x+self.y)


objc=C()
objc.m1()
objc.m2()
objc.m3()
'''

'''
#Hierarchical inhertance
class A:
    a,b=10,20               #Parent class
    def m1(self):
        print(self.a+self.b)

class B(A):
    m,n=50,60               #Child class
    def m2(self):
        print(self.m+self.n)

class C(A):
    x,y=90,110              #Child class
    def m3(self):
        print(self.x+self.y)

objb= B()
objb.m2()
objb.m1()

objc=C()
objc.m3()
objc.m1()
'''

#HMultiple inhertance
'''
class A:
    a,b=10,20               #Parent class
    def m1(self):
        print(self.a+self.b)

class B:
    m,n=50,60               #Parent class
    def m2(self):
        print(self.m+self.n)

class C(A,B):
    x,y=90,110              #Child class
    def m3(self):
        print(self.x+self.y)

objc=C()
objc.m3()
objc.m1()
objc.m2()
'''
#Hybrid Inhertance is combination of Hierarchical + Multiple

"""Super() keyword
is used to invoke 1) inovke parent class method
                  2) inovke parent class variable
                  3) inovke parent class constructor
"""

'''
class A:
    def m1(self):
        print('this is from Class A')

class B(A):
    def m2(self):
        print('this is from Class B')
        super().m1()            #calling parent class method using super

objb = B()
objb.m2()
'''

#accessing variable with super()
'''
a,b=20,30                   #global variable

class A:
    a,b= 33,44              #Parent class variable

class B(A):
    a,b=100,200             #child class variable
    def m1(self,a,b):       #method variable

        print(a+b)                  #caliing local variable
        print(self.a+self.b)        #calling child class var
        print(super().a+super().b)  #calling parent class var using super()
        print(globals()['a']+globals()['b'])    #calling global var

objb=B()
objb.m1(50,60)
'''

#calling constructor using super()
#if child class will not have any constructor, it will execute parent class constructor
#if child class will have any constructor, it will give priority to child class constructor and excute it
class A:
    def __init__(self):
        print('Parent class constructor')

class B(A):
    def __init__(self):
        print('child class constructor')
        super().__init__()              #calling parent class constructor using super()
        A.__init__(self)                #calling parent class constructor with class name

objb=B()