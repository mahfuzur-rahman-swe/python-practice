def hello(name):
    if not name:
        return "Hello every body!"

    else:
        return "Hello " + name

def showInfo(name, gender):
    print("Name: ", name);
    print("Gender: ", gender);




def showInfo(name, gender = "Male", country ="US"):
     print ("Name: ", name)
     print ("Gender: ", gender)
     print ("Country: ", country)



#modules
def sumValues(a, b, *others):

    retValue = a + b

 # 'others' parameter like an array.
    for other in others :
        retValue = retValue + other

    return retValue












