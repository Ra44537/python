# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "a")
# f.write("hello")
# f.close()




# with open("practice.txt","w") as f:
#     f.write("hi everyone \n we are learning File i/o \n using java. \n I like programming in java.\n")


# with open("practice.txt","r") as f:
#     data = f.read()
# data = data.replace("java","Python")    
# print(data)


# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != 1):
#         print("Found")
#     else:
#         print("not found")    


def check_for_line():
    word = "File"
    data = True
    line_no = 1
    with open("practice.txt") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1     

    return -1

check_for_line()         