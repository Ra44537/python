# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)


# show(5)        

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(4))



# def cla(n):
#     if(n==0):
#         return 0    
#     return cla(n-1) + n

# print(cla(5))   



def printl(list, id=0):
    if (id == len(list)):
        return
    print(list[id])
    printl(list, id+1)

fruits =["mango", "banana"]      

printl(fruits)