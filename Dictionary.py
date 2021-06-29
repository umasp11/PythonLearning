student= {'name':'uma', 'city':'BAM', 'Age':28}     #create dictionary
print(student)

student['name']='umasankar'                         #Modify dictionary
print(student)

#del student['Age']                                  #delete dictionary
#print(student)

for x in student:
    print(x,':', student[x])

#student.clear()             #delete everything from dict

print(len(student))

#print(student.popitem())                   #randomly return a item from dict and delete that
#print(student)

print(student.keys())                       #it will return all keys element in tuple
print(student.values())                     #it will return all values element in tuple

print(student.get('city'))                  # Return the value of that key

student.pop('Age')                          #remove that perticular key;value pair
print(student)