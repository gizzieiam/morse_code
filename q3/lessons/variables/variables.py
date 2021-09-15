# assign 4 to the variable x
x = 4

x = 1         # x is an integer
x = 'hello'   # now x is a string
x = [1, 2, 3] # now x is a list

y = x

print(y)

x.append(4)   # append 4 to the list pointed to by x
print(y)      # y's list is modified as well!

x = 'something else'
print(y)      # y is unchanged[1, 2, 3, 4]

# Python has types; however, the types are linked not to 
# the variable names but to the objects themselves.

x = 4
type(x)
int

x = 'hello'
type(x)
str

x = 3.14159
type(x)
float

# numerical types have a real and imag attribute that 
# returns the real and imaginary part of the value
x = 4.5
print(x.real, "+", x.imag, 'i')