# There are a couple of ways to create a dictionary — 
# using the literal syntax {}, or the built-in dict() 
# function.

# You can use either way to create an empty dictionary...

my_dict = {"one": 1, "two": 2, "three": 3}
            #  or
my_dict = dict(one=1, two=2, three=3)
print(my_dict)
# {'one': 1, 'two': 2, 'three': 3}


# Accessing a Dictionary
my_dict["one"]
# 1
# Adding keys to dic
my_dict["four"] = 4
print(my_dict)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# get() — retrieve a value from a dictionary
my_dict.get("one")
# 1
dict_items = {}
# items() — retrieve key/value pairs from a dictionary
my_dict.items()
dict_items([('one', 1), ('two', 2), ('three', 3)])
for pair in my_dict.items():
    print(pair)
# ('one', 1)
# ('two', 2)
# ('three', 3)

# keys() — retrieve the keys from a dictionary
dict_keys = ()
my_dict.keys()
dict_keys(['one', 'two', 'three'])
for key in my_dict.keys():
    print(key)
# one
# two
# three


# pop() — remove a key from a dictionary and return its corresponding value

# This method allows you to specify, as a second argument, a default value 
# to return in case the given key does not exist.

my_dict
# {'one': 1, 'two': 2, 'three': 3}
my_dict.pop("two")
# 2
my_dict
# {'one': 1, 'three': 3}
my_dict.pop("two", "nonexistent")
# 'nonexistent'

# setdefault() — retrieve a value from a dictionary, creating the key with a default value if the given key does not exist

my_dict
# {'one': 1, 'two': 2, 'three': 3}
my_dict.setdefault("two", 0)
# 2
my_dict.setdefault("zero", 0)
0
my_dict
# {'one': 1, 'two': 2, 'three': 3, 'zero': 0}


# values() — retrieve the values from a dictionary

# Notice the return value is an iterable that will produce one result at a time when looped over.
dict_values = ()
my_dict.values()
dict_values([1, 2, 3, 0])
for value in my_dict.values():
    print(value)
# 1
# 2
# 3
# 0

