fruitList = ["apple", "apricot", "banana", "coconut", "lemon", "plum", "pear"]
print ( fruitList )
print("\n")
# A sub list of elements with index from 1 to 4 (1, 2, 3)
subList = fruitList[1: 4]
print ("Sub List [1:4] ", subList )
print("\n")
print("fruitList[-1]:", fruitList[-1])
print("fruitList[-2]:", fruitList[-2])
print("\n")
subList = fruitList[-4:]
print(subList)
print("\n")
subList = fruitList[-4: -2]
print(subList)