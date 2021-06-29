def sum(start,end):
    result=0
    for i in range(start, end):
        result=result+i
    print(result)

sum(1,11)


def sum(start,end):
    result=0
    for i in range(start, end):
        result=result+i
    return result

s= sum(1,11)
print(s)

def named_arg(start, name, greeting):
    print(greeting + ' ',start +' '+ name)

#named_arg('uma', 'hi')  #Positional arg

#named_arg(name='sankar', greeting='hello')  #Keyword arg

named_arg('Mr', name='sankar', greeting='hello')    ##Positional arg + Keyword arg
#Positional arg must appear before keyword arg
