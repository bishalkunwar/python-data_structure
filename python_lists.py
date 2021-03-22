#Python code to implement lists:
#tuple is a sequence of immutable Python objects where as lists in mutable.

def array_container():
    #Creating lists:
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5 ]
    list3 = ["a", "b", "c", "d"]

    #Accessing elements in lists:
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7 ]
    print "list1[0]: ", list1[0]
    print "list2[1:5]: ", list2[1:5]

    #Updating lists:
    list = ['physics', 'chemistry', 1997, 2000]
    print "Value available at index 2 : "
    print list[2]
    list[2] = 2001
    print "New value available at index 2 : "
    print list[2]

    #Deleting lists elements:
    list1 = ['physics', 'chemistry', 1997, 2000]
    print list1
    del list1[2]
    print "After deleting value at index 2 : "
    print list1



array_container()