"""
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
syntax: filter(function, sequence)
function: function that tests if each element of a  sequence true or not.
sequence: sequence which needs to be filtered, it can  be sets, lists, tuples, or containers of any iterators.
"""
from _functools import reduce           #for reduce

seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


ages = [5, 12, 17, 18, 24, 32,19]
def myFunc(x):
  if x > 18:
    return True
  else:
    return False
adults = filter(myFunc, ages)
for x in adults:
  print(x)

"""
The map() function in Python takes in a function and a list as an argument. The function is called with a lambda function and a list 
and a new list is returned which contains all the lambda modified items returned by that function for each item.
syntax:   map(function, iterable(s))
"""

nums=[2,3,4,5,6,7,8,9]

even= list(filter(lambda x : x%2==0, nums))
print((even))

map_double= list(map(lambda x:x*3, even))
print((map_double))

#Reduce: it will add all the elements in a list
nums=[2,3,4,5,6,7,8,9]

even= list(filter(lambda x : x%2==0, nums))
print((even))
map_double= list(map(lambda x:x*3, even))
print((map_double))
sum=reduce(lambda a,b:a+b,map_double)
print(sum)

"""
The zip()function returns an iterator of tuples based on the iterable objects.
If we do not pass any parameter, zip() returns an empty iterator
If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
"""
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

result = list(zip(number_list, str_list))           #Output will in list format
print(result)

result = set(zip(number_list, str_list))            #Output will in set format
print(result)

result = dict(zip(number_list, str_list))           #Output will in dict format
print(result)