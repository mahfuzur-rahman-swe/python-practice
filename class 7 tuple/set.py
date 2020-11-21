'''my_set = {1, 2, 3}
print(my_set)
print("\n")
my_set = {"Hello",   (1, 2, 3),1.0}
print(my_set)

# set do not have duplicates
# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2} #duplicate value : 3, 2
print(my_set)

#my_set = {1, 2, [3, 4]}

my_set = set([1,2,3,2])
print("Covert list to set::",my_set)

a = set()
print(type(a))


my_set = {1,3}
print(my_set)
#add an element
my_set.add(2)
print("After add:: ",my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set = {1,3}
print(my_set)
my_set.update([2,3,4])
print('After add::',my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set = {1,3}
print("set: ", my_set)
my_set.update([4,5], {1,6,8})
print("List+Set = ",my_set)

my_set = {1, 3, 4, 5, 6}
print("Set:: ",my_set)
# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4) #want to delete 4 here from set
print("After discarding:: ",my_set)


my_set = {1, 3, 4, 5, 6}
print("Set:: ",my_set)
# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print("After Remove::",my_set)


# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld") #duplicate L, remove
print(my_set)


# pop an element
# Output: random element
my_set = set("HelloWorld")
print("Pop Data:: ",my_set.pop())


my_set = set("HelloWorld")
print("Set:: ",my_set)
# clear my_set
#Output: set()
my_set.clear()
print(my_set)


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("After Union:: ",A | B)

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use & operator
# Output: {4, 5}
print("After Intersection:: ",A & B)
'''

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use - operator on A
# Output: {1, 2, 3}
print("After Difference:: ", B-A) 
