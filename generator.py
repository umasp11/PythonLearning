#Generator are function that return sequence of values. we use yield statement to return the value from function
# yield statement return a values from a generator function into generator object   Ex: yield a
# next() function: is used to retrieve element by element from a generator object.    next(gen_obj)

# print result
def disp(a,b):
    yield a
    yield b

show=disp(10,20)
print(list(show))

#using next() method
def view(a,b):
    while a<=b:
        yield a
        a=a+1

result=view(2,10)
print(result)

print(next(result))
print(next(result))