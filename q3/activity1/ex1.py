#!usr/bin/env python
from platform import python_version

# This is my first python script!
print('--------------')
print('Python interpreter ' + python_version() + ' reporting for duty!')

# get a line of user text input
last_name = input('Enter your last name: ')
print('This ship is now commanded by Captain', last_name)