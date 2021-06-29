print('Program stated')
try:
    print(10/0)                 #it will throw zerodivisionerror
except ZeroDivisionError:
    print('Exception handled')
print('program completed')

print("**********************")

print('Program stated')
try:
    print(10/5)
except ZeroDivisionError:         #Except block will be exceuted only if we get any error
    print('Exception handled')
print('program completed')

print("**********************")

print('Program stated')
try:
    print(10/0)
except TypeError:
    print('TypeError Exception handled')
except ZeroDivisionError:                           #Whichever exception is caught, it will handle that
    print('ZeroDivisionError Exception handled')

print('program completed')
print('******************************')

# Try, except, else block. Else block will be excuted only when no except block matched or no exception occured
print('Program stated')
try:
    print(10/5)
except TypeError:
    print('TypeError Exception handled')
except ZeroDivisionError:
    print('ZeroDivisionError Exception handled')
except NameError:
    print('NameError Exception handled')
else:
    print('Else block excuted as no exception matched')
print('program completed')
print('******************************')

# Try, except, else, Finally block. finally block will be excuted regardless the result of try,except,else
print('Program stated')
try:
    print(10/0)
except TypeError:
    print('TypeError Exception handled')
except ZeroDivisionError:
    print('ZeroDivisionError Exception handled')
except NameError:
    print('NameError Exception handled')
else:
    print('Else block excuted as no exception matched')
finally:
    print('Finally block executed')
print('program completed')
print('*********************************************')
#Raise exception
def criteria(age):
    if age<0:
        raise ValueError('Value must be greater than 1')
    if age >=18:
        print('eligible to vote')
    if age <18:
        print('Not eleigible to vote')

num=criteria(-5)
print(num)