'''
File is of two types: text file-stores data in form of character
Binary file: stores data in form of bytes. like audio, video, image, PDF, csv
open(): is used to open a file. open('filename', mode= 'r' or 'w', buffering, encoding=None)
encoding- used to encode or decode the file. Ex: utf-8

r: open for reading, if file doesn't exist, it will show file not found error
w: Open for writing, if any data already present in file, it will overwrite the data, if the file doesn't exist, it will create the file
x: Open for exclusive creation with write. the specified file must not be available. if its available it will show fileExistsError
a: Open for appending, pointer will be positioned at the end of the file and it appends new data at the end of the line. if the file doesn't exist, it will create the file
r+: Open for reading and then writing
w+: open for writing and then reading. it will overwrite existing data
a+: Open for appending then reading. it wont overwrite existing data

'''



import os

#read
f= open("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\file.txt", 'r')
print(f)                            #it will print the path of file
data=f.read()                       #it will read/print the data
print(data)

#Write
f= open("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\student.txt", 'w')
f.write('hello user \n')
f.write('welcom to python')
f.close()

#Writelines
f= open("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\student1.txt", 'w')
list=['uma\n', 'sankar\n', 'panigrahy\n']
f.writelines(list)
f.close()
print('confirmation msg of success')

#will return True if file exists
print(os.path.isfile("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\file.txt"))
#os.remove(("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\demo.txt"))      #To remove file

#open("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\demo1.txt", 'x') # new file will created, 'x' is used to create new file

#file.write('First line\n')
#file.write('Second line\n')

#print(file.read())         #print the whole file

#print(file.read(2))        #pint first two char

#print(file.readline())     #read the first line

#print(file.readlines())     #Read whole content in array format
#for line in file:
#    print(line)

#file.write('this is 6th line')      #to write content into file & in maine file use 'a' for append

