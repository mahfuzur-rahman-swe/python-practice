'''info = {"name": "Mahfuzur Rahman", "Id": "172-35-2207", "Department": "Software Engineering"}
print(info["name"])

mydict = dict()

mydict["01"] = "John"
print(mydict)

info = {"name": "Mahfuzur Rahman", "Id": "172-35-2207", "Department": "Software Engineering"}

print("Name: ", info["name"])

# update dictionary

info = {"name": "Mahfuzur Rahman", "Id": "172-35-2207", "Department": "Software Engineering"}

info["name"] = "Tipu Sultan"
print(info["name"])

info = {"name": "Mahfuzur Rahman", "Id": "172-35-2207", "Department": "Software Engineering"}
print("Element count: ", len(info))

#Delete dictionary
info = {"name": "Mahfuzur Rahman", "Id": "172-35-2207", "Department": "Software Engineering"}
del info["name"]
print(info)
#or delete key by method
info.__delitem__("Id")
print("After Id delete: ", info)

# Clear all element
info = {"name": "Mahfuzur Rahman", "Id": "172-35-2207", "Department": "Software Engineering"}
info.clear()
print(info)
#or
del info
'''
