#What happens in the background when you run a python file?
'''When we run a .py file, it undergoes two phase 1st it checks the syntax and second it compiles to bytecode(.pyc file is generated) using
python virtual machine and loads the bytecode into memories and run'''

'''How to connect to oracle data base using python script
import os
import cx_Oracle        #It is a Python extension module that enables access to Oracle Database.
set folder in which instant client is installed in syastem path
os.environ['path']=c:\desktop\instance.client.18.3
connection=cx_Oracle.connect(''hr', 'userpwd', 'example.com/orclpdb1')
cursor=connection.cursor()'''


a=10,20,'uio'
print(type(a))      #datatype
print(id(a))        #Identyfier
print('****************************************************')

#swap two number using 3rd variable
a=10
b=20
a,b=b,a
print('a=',a)
print('b=',b)
print('****************************************************')

import sys
print(sys.version)
print('****************************************************')

#convert a list of integers to a comma separated string
a=[1,2,3,4,5,6,7]
nummbers= ','.join(str(i) for i in a)
print(nummbers)
print('****************************************************')

li= ['78', '10', '50','20']
new= [int(z) for z in li]
print(sorted(new))
print('****************************************************')

#Create a list which is reversed version of another list
li=[10,20,30,50,60,70]
new=list(reversed(li))
print(li)
print(new)
print('****************************************************')

#print the name from list where the name start with 'S'
nmaes=['samson', 'dravid', 'kohli', 'sachin', 'kumbble', 'sehwag']
sname= [name for name in nmaes if name[0]=='s']
print(sname)
print('****************************************************')
#print different(unique) character from the string and their count
s= 'this is a simple set to count the number of chracter and their count'
print(set(s))               #it will show the unique character
print(len(set(s)))          #print the total unique count
print('****************************************************')

import random
print(random.random())      #random number will given between 0 & 1
print(random.randint(9,78)) #random int number will be printed
print('****************************************************')

from random import shuffle
x=['wellcom', 'india', '222', 'python', 'fly']
shuffle(x)
print(x)
print('****************************************************')

#How too print current date & time
from datetime import datetime,date

now = datetime.now()
today=date.today()

#current time
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#current datetime
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
