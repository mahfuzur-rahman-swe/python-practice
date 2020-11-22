import test

print("By this system, you can do........")
print("1. Add data\t" + "2. Display\t" + "3. Search\t" + "4. Edit\t" + "5. Delete")

press = input("Do you want to enter this system, y/n?:: ")
if press == "y" or input == "Y":
    print("Successfully entered this system.....")
    file = open("test.txt", "a")
    while press:
        print("Now choose option")
        choice = int(input("1. Add\t" + "2. Display\t" + "3. Search\t" + "4. Edit\t" + "5. Delete\t" + "6. Exit\n" + "Select Option:: "))

        if choice == 1:
            keyValue = input("Enter your key here: ")
            Value = input("Enter your you value for " + keyValue + ":: ")
            file.write(file[keyValue])
            file.close()

        if choice == 2:
            press =

else:
    print("You wanted to exit!!")