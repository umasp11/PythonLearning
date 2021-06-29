"""it is datatype which represents a group of element in key value pairs. Mutable, case sensitive
Dictionary in python is unordered collection"""

student={'name':'uma', 'id':11, 'adress':'bam'}
student['name']='sankar'
print(student)

#To add/insert key:value pair
student['job']= 'eng'
print(student)

#Access from dictionary and return in dictionary
student={'first':'uma', 'id':11, 'adress':'bam', 'new':{'course':'python', 'fees':22000}}
li=student['first']
print(li)       #op: uma
li1= student['new']['course']
print(li)       #python
tl={li:li1}
print(tl)       #op:{'uma': 'python'}

# Add value in a nested dict
student={'first':'uma', 'id':11, 'adress':'bam', 'new':{'course':'python', 'fees':22000}}
student['new']['loc']= 'goa'
print(student)

# Add dict in a nested dict
student={'first':'uma', 'id':11, 'adress':'bam', 'new':{'course':'python', 'fees':22000}}
student['new1']= {'first':'uma', 'id':11, 'adress':'bam'}
print(student)


#access key/value in nested dictionary
student={'first':'uma', 'id':11, 'adress':'bam', 'new':{'course':'python', 'fees':22000}}
li= student['new']['course']
print(li)


#get() method: returns the value of specified key
new_student= {'name':'usp', 'id':12, 'adress':'bbsr'}
print(new_student.get('name'))

#items()
student={'first':'uma', 'id':11, 'adress':'bam'}
li=student.items()
new_li=list(li)                #dict is not subscriptable i.e [] so we need to convert it to list first
print(new_li[0])

#Keys(): this will return all the key element of the dictionary
student={'first':'uma', 'id':11, 'adress':'bam'}
dict_key=list(student.keys())
print(dict_key)

#Values(): this will return all the value element of the dictionary
student={'first':'uma', 'id':11, 'adress':'bam'}
dict_value=list(student.values())
print(dict_value)

#update()
data={'job':'eng', 'mob':123, 761:'pin'}
student={'first':'uma', 'id':11, 'adress':'bam'}
student.update(data)
print(student)

#copy
student={'name':'uma', 'id':11, 'adress':'bam'}
new=student.copy()
print(new)

#Access dictionary using for loop
student={'name':'uma', 'id':11, 'adress':'bam'}
for k in student:
    print(k, '=', student[k])       #k will print key and student[k] will print value