'''def sum(*ab):
    s=0
    for i in ab:
        s=s+i
    print('sum is', s)

sum(20,35,55,90,140)
'''


'''def myarg(a,b,c,d,e):
    print(a,b,e)

list=[10,15,30,50,77]       #no of parameter should be same as no of arguments

myarg(*list)'''

#Keyword argument **
def myarg(a,b,c):
    print(a,b,c)

li={'a':10, 'b':'hello', 'c':100}

myarg(**li)

    #OR

def myarg(a=10,b=11,c=15):
    print(a,b,c)


myarg()

    #OR

def myarg(**keywords):
    for i,j in keywords.items():
        print(i,j)

myarg(name='Kohli', sport= "Cricket", age=30)

#Lambda Function
result= lambda a:a*10
print(result(5))

#OR

def myfun(n):
    return lambda a: a*n
result= myfun(5)

print(result(10))