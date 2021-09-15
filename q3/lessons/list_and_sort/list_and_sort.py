# Lists are mutable — they can be directly modified in 
# place in your computer's memory without a new list 
# object being created.

# Lists are sequences — their contents are ordered and 
# can be accessed by their position within the sequence,
#  called an index.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
print(my_list[8])

#  my_list.clear() - removes all items from a list
# my_list2 = my_list1.copy() - make a cody of a list
# my_list.append(3) - adds an item to the end of a list


# Because Python uses variable names as object references,
#  and mutable objects (such as lists) can be modified 
# in-place without requiring reassignment, you will 
# usually want to copy a list rather than simply assign 
# an additional name to it.

my_list1 = [1, 2, 3]
my_list2 = my_list1  # now they're identical
print(my_list1, my_list2)
# [1, 2, 3] [1, 2, 3]
my_list1.append(4)  # should only affect my_list1...right?
print(my_list1, my_list2)
# [1, 2, 3, 4] [1, 2, 3, 4]  # oops -- changed both of them!

# my_list.count(3) - count number of occurrences of a value from a list
# my_list.extend([4, 5, 6]) - add items from an iterable to the end of a list

# It can be easy to mix up extend() and append(), since 
# they both add to the end of a list. Try to remember 
# that append() adds the whole object to the list...

# append
list = [1]
list.append([2, 3])
print('appended list: ' + str(list))
# extend
list2 = [1]
list2.extend([2, 3])
print('extended list: ' + str(list2))

# my_list.index(2) -  get the index of the first occurrence of a value from a list
# my_list.insert(1, 2) - add an item at any position in a list
# my_list.pop(0) - remove and return an item from any position in a list
# my_list.remove(3) - remove the first occurrence of a value from a list
#  my_list.reverse() -  reverse the order of the items in a list


### SORTING

# my_list.sort() - sort an iterable's items and return them as a list
# sorted() function takes an iterable and returns a list of its sorted items.

# key -  a function that will be applied to each item, 
# with its result used as the sorting value

my_list = ["hello", "hi", "greetings", "hey"]
my_list.sort(key=len)
my_list
# ['hi', 'hey', 'hello', 'greetings']


# my_list.sort(reverse=True) - a boolean flag for specifying the order (direction) of the sorting