'''OOPs is programmimng model oragnized around OBJECTS and DATA rather than ACTIONS an LOGIC
uses DRY method: Dont repeat yourself, code wont repeated

instance varibale: these are defined and initialized using a constructor with self parameter
Instance method is used to access instance variable (create another simple method to access constructor from where we can access instance variable)
class/static variable: which is declared inside class and outside method. We can access class variable by using class method. ex: cls.v

Types of method: Instance, class, static
__init__: is a reseved method in python classes. which is called as a constructor  This method is called when an object is created from a class.
self- self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
'''


student={'first':'uma', 'id':11, 'adress':'bam', 'new':{'course':'python', 'fees':22000}}
student['new']['new1']= {'first':'uma', 'id':11, 'adress':'bam'}
print(student)







