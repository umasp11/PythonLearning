'''
#self parameter is a reference that the method belongs to the class
class calculator:
    num=100                     #Class variable

    def add(self):              #method
        print('this is method')

ob=calculator()                 #Creating object for class to call method/variable
ob.add()                        #calling method
print(ob.num)                  #calling variable

#OP:
#this is method
#100
'''

'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person

print(p1.name)
print(p1.age)
'''


#The self parameter does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
'''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc, na,  old):
    print("Hello my name is " + na, 'i am' + str(old))

p1 = Person('uma', 33)
p1.myfunc('umasankar',22)

#OP: Hello my name is umasankar i am22
'''

"""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#OP: Hello my name is John
"""


'''class Person:
    def empty(self):
        pass

    def myfunc(self, name):
        print("Hello my name is ", name)

p1 = Person()
p1.myfunc('umasankar')'''


'''
# Static\Instance\class method
class insta:                        #when we create method inside the class by default is called instance method
    def instance(self):
        print('instance method')

    @staticmethod                   #to define static method we need to we need setup this
    def static():                   #static method doesnt take any parameter(self), if it takes an param we need to pass some argument while calling this methdd
        print('static method')
        
    @classmethod                    #ClassMethod
    def classname(cls,name):
        cls.name=name

ob= insta()
ob.instance()
insta.static()                      # to call static method no need to use object, it can be called directly from class
'''

'''
#class variable
class calculator:
    a,b=20,30

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)

ob= calculator()
ob.add()
ob.mul()
'''

'''
#Local, class, Global variable

a,b=20,30                       #gloval variable
class calculator:
    c,d= 50,60                  #class variable

    def add(self,e,f):          #local variable
        print(e+f)              #accessing local variable
        print(self.c+self.d)    #accessing class variable
        print(a+b)              #accessing global variable

ob= calculator()
ob.add(90,100)
'''

'''
#If Local, class, Global variable name are same

a,b=20,30                       #gloval variable
class calculator:
    a,b= 50,60                  #class variable

    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+ globals()['b'])        #use global keyword to accessing global variable

ob= calculator()
ob.add(90,100)
'''

'''
#Multiple objects for same class
class calculator:
    a,b=20,30

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)

ob= calculator()            #1st object for same class
ob1=calculator()            #2nd object for same class

ob.add()                    #named object
ob1.mul()                   #named object

calculator().add()          #nameless object
'''

'''
#Constructor
class const:

    def m1(self):
        print('this is method')

    def __init__(self):
        print('this is contructor')

ob=const()              #constructor willautomatically invoked when object is creted
ob.m1()
'''

'''
#converting local var into class var
class calculator:
    def m1(self,a,b):
        print(a)
        print(b)
        self.a=a        #assigning local into class var
        self.b=b        #assigning local into class var

    def add(self):
        print(self.a+self.b)        #Local var

ob=calculator()
ob.m1(20,30)
ob.add()
'''

'''
class calculator:
    def __init__(self,a,b):
        print(a)
        print(b)
        self.a=a        #assigning local into class var
        self.b=b        #assigning local into class var

    def add(self):
        print(self.a+self.b)        #Local var

ob=calculator(20,30)        #passing the 2 constructor arg
ob.add()
'''

'''
#Calling a method from another method
class student:
    def m1(self):
        print('this is method 1')
        self.m2('umasankar')

    def m2(self, name):
        print('student name is ', name)

ob=student()
ob.m1()
'''

'''
#Passin arg into constructor
class student:
    name= 'sankar'

    def __init__(self,name):
        print(name)             #contsructor/local var called
        print(self.name)        #global variable called

ob=student('uma')
'''

'''
#Employees example
class emp:
    def __init__(self, id, name, sal):
        self.id=id
        self.name=name
        self.sal=sal

    def display(self):
        print('id:{} name:{} sal{}'.format(self.id,self.name,self.sal))
        print(self.name, 'has ', self.sal, 'salary')

ob=emp(11, 'usp', 10)
ob.display()
'''

'''
#__str__ method: when object id created it will inovoke automatically and print the method
class emp:
    def __init__(self, id, name, sal):
        self.id=id
        self.name=name
        self.sal=sal

    def __str__(self):
        return ('id:{} name:{} sal{}'.format(self.id,self.name,self.sal))


ob=emp(11, 'usp', 10)
print(ob)
'''

##__del__ method: will invoked when object is destoyed

class student:
    def __del__(self):
        print('destroyed')

ob1=student()
ob2=student()


