# Tuples (pronounced TOO-pulls), like lists, are one of 
# Python's basic sequence data types. They differ from 
# lists, however, in that they are immutable. They are 
# the perfect data type for when you need to store data 
# together in a way that cannot be modified

## ie.. tuples not changable; list is changable

animals = ("dog", "cat", "squirrel")  # a tuple created using parentheses
type(animals)

# count() — return the number of occurrences of a given value in the tuple
nums = (11, 33, 42, 50, 33, 98)
nums.count(33)
# 2