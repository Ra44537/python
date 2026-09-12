# Light = input("Light:")
# if(Light == "red"):
#     print("stop")
# elif(Light == "yellow"):
#     print("wait for green")
# elif(Light == "green"):
#     print("go")
# else:
#     print("light is broken")            


# marks = int(input("marks:"))
# if(marks >= 90):
#     print(" a grade")
# elif(marks >= 80 and marks <90):
#     print("b grade")
# elif(marks >= 70 and marks <80):
#     print("c grade")
# else:
#     print("D") 

A = int(input("A:"))
B = input("M/F :")
if((A == 1 or A == 2) and B == "M"):
    print("fees is 200")
elif(A == 3 or A == 4 or B == "F"):
    print("fees is 200")
elif(( A ==5) and B == "M"):
    print("fees is 300")
else:
    print("no fees")            