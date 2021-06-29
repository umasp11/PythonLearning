list= ['python', 200, 'Age', 'fruit', 'address', 'Age']
list2=['Java', 'city', 4000]

for i in list:
    print(i,end= ' ')


list.append(20.5)
print(list)

print(list.count('Age'))

list.extend(list2)
print(list)

print(list[4])

print(list.index('fruit'))

list.insert(1, 'name')
print(list)

#pop used to remove the last element and also if we give any position, it will remove elemnt from that position
list.pop(2)
print(list)

list.remove('Age')
print(list)

# list.clear() will remove all the contents from list

list.reverse()
print(list)


# List Comprehension:
list= [x for x in range(0,10,3)]
print(list)

[print(x, end=' ') for x in range(50) if x%5==0]
print(end='\n')

fruits= ['apple', 'mango', 'cherry', 'kiwi']
newfruits=[]

for x in fruits:
    if 'a' in x:
        newfruits.append(x)
print(newfruits)
print(end='\n')

[print(x, end=' ') for x in fruits if 'e' in x]     # e latter fruit will be returned
print(end='\n')

newfruits = [x for x in fruits if x != "apple"]     #except apple everything will be printed
print(newfruits)

[print(x.upper(), end=' ') for x in fruits]         #print in uppercase
print(end='\n')

[print('hello', end=' ') for x in fruits]           # 5 time hello will be printed
print(end='\n')

fruits.sort()                                   #sort
print(fruits)

fruit1= fruits.copy()
print(fruit1)

l1= ['a','b','c']
l2= [1,2,3]
l1.extend(l2)
print(l1)
#method 2: print(l1+l2)