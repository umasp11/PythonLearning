'''#Approach 1

from Module import Operation

Operation.add(10,11)
Operation.mul(10,11)

#Approah 2
from Module.Operation import add,mul,sub
add(20,21)
mul(20,21)

#Appoach
from Module import *            #all functions will be imported
add(20,21)
mul(20,21)
sub(20,9)
'''

#approach1
'''from Module import animalclass      #import the classname from module

obj=animalclass.animal()             #create object for the class to call the method
obj.nonveg()
obj.veg()
'''

#approach 2
from Module.animalclass import animal
obj=animal()
obj.veg()