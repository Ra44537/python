# marks = [94.4, 87.4, 91, 98,92]
# print(marks)
# print(marks[0])
# print(marks[1:5])
# print(type(marks))

# student = ["karan", 95.4, 95, "Delhi"]
# print(student[0])
# student[0] = "arjun"
# print(student)

# tup = (1, 2, 3, 4,4, 5)
# print(tup.count(2))
# print(type(tup))
# print(tup.count(4))
# print(tup.index(4))


#enter a movies in list 
# movies = []
# mov1 = input("enter1")
# mov2 = input("enter2")
# movies.append(mov1)
# movies.append(mov2)
# print(movies)


#palindrome 
list1 = [1,2, 1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not a palindrome")