for letter in "hello":
    print(letter)

for _ in range(3):
    print("Options:\n1 - Do\n2 - Do Not\n3 - Try")
    choice = int(input("Choose one: "))
    if choice == 1:
        print("Yes. Good.\n")
        break
    elif choice == 2:
        print("That is why you fail.\n")
    elif choice == 3:
        print("Do. Or do not. There is no Try.\n")
    else:
        print("You seek Yoda.\n")

# enumerate() — retrieve both an index and a value 
# from an iterable
found = False
nums = [3, 4, 7, 2, 8, 4, 6]
for i, num in enumerate(nums):
    if i > 0 and num + nums[i-1] == 10:
        found = True

print(found)

# range() — generate a sequence of integers based on 
# the values given
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11, 3):
    print(i)

# The while loop is used when you want to keep doing 
# something as long as a condition is true or until the 
# loop is ended manually. Its syntax consists of the 
# while keyword, followed by an expression that evaluates
#  to True or False.

countdown = 3
while countdown > 0:
    print(countdown, "...", sep="")
    countdown -= 1

print("Blast off!")

choice = None
while choice != 1:
    print("Options:\n1 - Do\n2 - Do Not\n3 - Try")
    choice = int(input("Choose one: "))
    if choice == 1:
        print("Yes. Good.\n")
    elif choice == 2:
        print("That is why you fail.\n")
    elif choice == 3:
        print("Do. Or do not. There is no Try.\n")
    else:
        print("You seek Yoda.\n")