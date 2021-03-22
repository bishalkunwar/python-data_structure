#Python code implementing arrays:
from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
 print(x)


#Accessing array elements:
print (array1[0])
print (array1[2])

#Inserting the array elements:
array1.insert(1,60)
for x in array1:
    print(x)

#Deletion operation:
array1.remove(40)
for x in array1:
    print(x)


#Search operation;
print (array1.index(40))

#Update operation:
array1[2] = 80
for x in array1:
    print(x)

