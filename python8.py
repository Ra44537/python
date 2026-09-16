#Dictionary
# info = {
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4,
#      "subjects" : ["python", "C", "Java"],
#      "topic" : ("dict", "set"),
#      12 : 94.4
# }

# info["name"] = "Raj"
# info["surname"] = "Malviya"
# print(info)

#Nested Dictionary
# student = {
#     "name" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem ": 92,

#     }
# }
#print(student)
#print(student["subjects"])
# print(student["subjects"] ,["chem"])

##### SET #####
# collection = { 1, 2, 3, 4}

# print(collection)
# print(type(collection))

# collection = {1, 2, 3, 4, 5}
# collection2 = { 1, 2, 6, 7, 8, 9}
# print(collection.union(collection2))
# print(collection.intersection(collection2))


# collection = set()
# collection.add("a piece of furniture")
# collection.add("list of facts & figures")
# print(collection)

# set1 = {"python", "java", "C++", "python", "javascript","java", "C++", "python","C"}

# print(set1)

marks = {}
x = int(input("enter py"))
marks.update({"py" :x})
y = int(input("enter ch"))
marks.update({"ch" : y})

print(marks)