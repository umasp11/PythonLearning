import os
import csv
import io
import codecs

f=  open("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\test.csv", 'r')
reader=csv.reader(f)
li=[]
for row in reader:
    li.append(row)
    print(row)
print(li)

# write method
f1=open("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\test1.csv", 'w')
new=['tom', 'US', 30]
writer= csv.writer(f1)
writer.writerow(new)

# write method
f1=open("C:\\Users\\umasankar.panigrahy\\Desktop\\Docker\\PM\\test.csv", 'a')
new=['tom', 'US', 30]
writer= csv.writer(f1)
writer.writerow(new, delimiter=',')

