'''file = open("Demo.txt", "w")
file.write("This is first line\n")
file.write("this is second line\n")
file.write("this is third line\n")
file.write("this is fourth line")
file.close()
file = open("Demo.txt", "d")
print(file.readline(2))

file = open("Demo.txt", "r")
print(file.read())
file.close()
file = open("Demo.txt", "r")
print("\n",file.read(10))
file.close()

#If we wanted to return only the 2nd line in the file, we would use this:
'''


file = open("demo2.txt","w")
file.write("Hello World\n")
file.write("This is our new text file\n")
file.write("and this is another line.\n")
file.write("Why? Because we can do it this easily.")
file.close()
file = open("Demo2.txt", "r")
print("\n", file.readline(2))



'''file = open("Demo2.txt", "r")
for x in file:
    print(x)'''


