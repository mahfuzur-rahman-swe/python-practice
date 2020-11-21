inp = int(input("How many layer you want:"))

chicken = 0
egg = 0
spicy = 0

for i in range(inp):

    value = int(input("1-chicken petty  or 2-Egg or 3-Spicy:"))

    if value == 1:
        print("A petty of chicken will be added")
        chicken += 1
    elif value == 2:
        print("A petty of Egg will be added")
        egg += 1
    elif value == 3:
        print("Spicy will be added")
        spicy += 1
    else:
        print("Enter only 1 or 2 or 3")

if chicken > egg:
    print("Melay Jai re")