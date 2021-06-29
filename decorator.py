# reference: Geeky shows: Decorator Is a function that takes another function as argument, add some kind of functionalities and returns another function

def decor(fun):
    def inner():
        print('this inner fun will excute before enhance method')
        fun()
        print('after enhance method this inner fun will be excuted')
    return inner

#@decor                                              #this is decorator
def enhance_method():
    print('this method will be emhnacened in decor method')

#enhance_method()

result= decor(enhance_method)           # we can call decorator like this also
result()

print("***********************************")

# example2: A main function there with 10, returm 15 without modifying main method

def decor(fun):
    def inner():
        a=num()
        add= a+5
        return add
    return inner

def num():
    return 10


result= decor(num)
print(result())


# example3: A main function there with 10, first requirement was to change it to 50 then change it to 500
def decor1(num):
    def inner():
        a=num()
        mul= a*5
        return mul
    return inner

def decor2(num):
    def inner():
        b=num()
        mul= b*10
        return mul
    return inner


def num():
    return 10

result= decor2(decor1(num))
print(result())