"""
Shallow Copy
A shallow copy creates a new object which stores the reference of the original elements.
So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects.
it will create new and independent object with same content.
"""

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
print("Old list:", old_list)
print("New list:", new_list)


'''
In the below program, we made changes to old_list i.e old_list[1][1] = 'AA'. Both sublists of old_list and new_list at index [1][1] were modified. 
This is because, both lists share the reference of same nested objects.
'''
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)


#A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

'''In the above program, we use deepcopy() function to create copy which looks similar.
However, if you make changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.'''


old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'
print("Old list:", old_list)
print("New list:", new_list)

'''In the above program, when we assign a new value to old_list, we can see only the old_list is modified. This means, both the old_list 
and the new_list are independent. This is because the old_list was recursively copied, which is true for all its nested objects.'''
