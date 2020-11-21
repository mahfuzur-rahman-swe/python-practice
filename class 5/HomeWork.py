print("You can do.....")
print("Add Data")
print("Display Data")
print("Search Data")
print("Edit Data")
print("Delete Data")
print("Exit\n")

inp = int(input("How many layer do you want? "))

fruit = []

for x in range(inp):
    choice =  int(input("1. Add" + "\t" + "2. Display" + "\t" + "3. Search"
               + "\t" + "4. Edit" + "\t" + "5. Delete" + "\t" + "6. Exit" + "\n" +
                         "Enter your choice: "))

    if choice == 1:
        run = int(input("\nHow many fruit, Do you want to add?" + "\n" + "Enter a number: "))
        for m in range(0, run):
            value = input("Enter fruit name: ")
            fruit.append(value)

    elif choice == 2:
        print("Fruit List = ", fruit)
        print("\n")

    elif choice == 3:
        put = int(input("Enter index number: "))
        if fruit:
            print("\nSearch Result: ", fruit[put] + "\n")

        elif put not in fruit:
            print("No fruit available")

    elif choice == 4:
        inp = int(input("Enter fruit index number: "))
        print("\nYou want to change:: ",fruit[inp])
        if fruit:
            name = input("\nEnter new name: ")
            fruit[inp] = name
            print("\nNew Fruit List = ", fruit)

        elif inp not in fruit:
            print("No fruit available at ", inp)

    elif choice == 5:
        inp = input("Enter fruit name: ")
        if inp in fruit:
            fruit.remove(inp)
            print("\nNew Fruit List = ", fruit)

        else:
            print("Not matching!")
            print("Select again for remove\n")

    elif choice == 6:
        print("You wanted to exit!")
        break

else:
    print("\nYou have no selection!")



