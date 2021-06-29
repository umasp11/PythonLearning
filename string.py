'''name = 'welcome to python'

print(type(name))               #data type

print(id(name))                 #Location id

print( name * 3)                #multiplication

print('Welcome to '+ name)      #concatenation

print(name[1:4])                #slicing
print(name[:5])                 #slicing from start to index 5
print(name[5:])                 #slicing start from 5 to end

print(ord('Y'))                 #returns ASCII number of char
print(chr(70))                  ##returns char of ASCII number

print(len(name))                #string length function
print(max(name))                #String max function
print(min(name))                ##String min function

print('py' in name)             #IN operator
print('hello' not in name)      #not in operator

print('a'<'b')                  #Comparison operator
print('B'== 'b')                #Comparison operator
print('Python'>= 'java')         #Comparison operator

for i in name:                  #For iterative loop
    print(name, "test")

print(name.isalnum())           #Returns True if string is alphanumeric
print(name.isalpha())           #Returns True if string is only alphabets
print('2020'.isdigit())         #Returns True if string contains only digit
print(name.islower())           #Returns True if string is in lower case
print('WELcome'.isupper())      #Returns True if string contain only upper case
print(" ".isspace())            #Returns True if string contains whitespace

print(name.startswith('wel'))   #Returns True if string start with wel
print(name.endswith('on'))      #Returns True if string ends with on
print(name.find('ome'))        #Returns the index number from where string starts
print(name.count('o'))          #retuns the count of character

print(name.capitalize())        #Return a string with first lettr capitalized
print(name.title())             #Return the string by capitalizing first letter of every word of string
print(name.lower())             #Return string by converting all character into lowercase
print(name.upper())             #Return string by converting all character into uppercase
print(name.swapcase())          #convert lower to upper and upper to lower
print(name.replace('on','in'))  #replaces certain character into different character

print(name.strip())             #Remove whitespace from beginning or end
print(name.split())             # returns a list of word by from the string




name.sort       #Ascending

name.sort (reverse=True)        #descending



'''